# RPG MAKER ADAPTER

Instrumentation and defect catalog for RPG Maker MV/MZ games.

## Detection

Confirm RPG Maker usage:

```bash
# File system signals
find . -name "Game.rgss*.js" -o -name "www" -type d -o -name "nw.exe"
find . -name "Data/*.json" -o -name "js/*.js"

# Binary signals
file nw.exe  # NW.js executable
ls -la www/  # Web assets folder
```

```javascript
// Code signals
// Game.rgss1.js, Game.rgss2.js, Game.rgss3.js
// RPGMV or RPGMZ in code
```

```javascript
// Runtime signals
// RPG Maker games run in NW.js (Chromium + Node.js)
// Access via nw.Window.get()
```

## Instrumentation Options

### Option 1: Plugin Injection (Best)

RPG Maker games support JavaScript plugins. Inject custom plugin for instrumentation:

```javascript
// plugins/PLAB_Debug.js
/*:
 * @plugindesc PLAB Debug Plugin
 * @author PLAB
 *
 * @param DebugMode
 * @desc Enable debug mode
 * @type boolean
 * @default true
 */

(function() {
    'use strict';

    const parameters = PluginManager.parameters('PLAB_Debug');
    const debugMode = parameters['DebugMode'] === 'true';

    if (!debugMode) return;

    // Expose game state
    window.PLAB = {
        game: null,
        scene: null,
        party: null,
        player: null,

        init: function() {
            this.game = window.nw ? nw.Window.get() : null;
            this.scene = SceneManager._scene;
            this.party = $gameParty;
            this.player = $gamePlayer;
        },

        getState: function() {
            return {
                mapId: $gameMap.mapId(),
                mapName: $gameMap.displayName(),
                playerX: $gamePlayer.x,
                playerY: $gamePlayer.y,
                playerDir: $gamePlayer.direction(),
                gold: $gameParty.gold(),
                items: $gameParty.items().length,
                weapons: $gameParty.weapons().length,
                armor: $gameParty.armors().length,
                members: $gameParty.members().length,
                switches: $gameSwitches,
                variables: $gameVariables,
                time: $gameTimer,
                battle: $gameTroop.isEscaped()
            };
        },

        getMapEvents: function() {
            const events = [];
            $gameMap.events().forEach(event => {
                if (event) {
                    events.push({
                        id: event.eventId(),
                        name: event.event().name,
                        x: event.x,
                        y: event.y,
                        page: event._pageIndex
                    });
                }
            });
            return events;
        },

        getItems: function() {
            return $gameParty.items().map(item => ({
                id: item.id,
                name: item.name,
                quantity: $gameParty.itemQuantity(item),
                price: item.price,
                consumable: item.consumable
            }));
        },

        getWeapons: function() {
            return $gameParty.weapons().map(weapon => ({
                id: weapon.id,
                name: weapon.name,
                attack: weapon.params[2],
                price: weapon.price
            }));
        },

        getArmor: function() {
            return $gameParty.armors().map(armor => ({
                id: armor.id,
                name: armor.name,
                defense: armor.params[1],
                price: armor.price
            }));
        },

        getActors: function() {
            return $gameParty.members().map(actor => ({
                id: actor.actorId(),
                name: actor.name(),
                hp: actor.hp,
                mp: actor.mp,
                level: actor._level,
                exp: actor._exp[actor._level],
                state: actor.isStatesAffected() ? actor.states() : []
            }));
        },

        getMapName: function() {
            return $gameMap.displayName();
        },

        getMapId: function() {
            return $gameMap.mapId();
        },

        getPlayerPosition: function() {
            return {
                x: $gamePlayer.x,
                y: $gamePlayer.y,
                direction: $gamePlayer.direction(),
                screenX: $gamePlayer.screenX(),
                screenY: $gamePlayer.screenY()
            };
        },

        getSwitch: function(id) {
            return $gameSwitches.value(id);
        },

        setSwitch: function(id, value) {
            $gameSwitches.setValue(id, value);
        },

        getVariable: function(id) {
            return $gameVariables.value(id);
        },

        setVariable: function(id, value) {
            $gameVariables.setValue(id, value);
        },

        getGold: function() {
            return $gameParty.gold();
        },

        setGold: function(amount) {
            $gameParty.gainGold(amount - $gameParty.gold());
        },

        addItem: function(itemId, quantity) {
            const item = $dataItems[itemId];
            if (item) {
                $gameParty.gainItem(item, quantity);
                return true;
            }
            return false;
        },

        removeItem: function(itemId, quantity) {
            const item = $dataItems[itemId];
            if (item && $gameParty.itemQuantity(item) >= quantity) {
                $gameParty.loseItem(item, quantity);
                return true;
            }
            return false;
        },

        teleport: function(mapId, x, y) {
            $gamePlayer.reserveTransfer(mapId, x, y, $gamePlayer.direction());
            SceneManager.goto(Scene_Map);
        },

        saveGame: function(slotId) {
            DataManager.saveGame(slotId);
        },

        loadGame: function(slotId) {
            DataManager.loadGame(slotId);
        },

        getSaveSlots: function() {
            const slots = [];
            for (let i = 1; i <= 20; i++) {
                if (DataManager.isThisGameFile(i)) {
                    slots.push(i);
                }
            }
            return slots;
        },

        getBattleState: function() {
            if (!$gameTroop) return null;
            return {
                inBattle: $gameTroop.isEscaped() === false,
                turnCount: $gameTroop._turnCount,
                enemies: $gameTroop.members().map(enemy => ({
                    id: enemy.enemyId(),
                    name: enemy.name(),
                    hp: enemy.hp,
                    mp: enemy.mp,
                    state: enemy.isStatesAffected() ? enemy.states() : []
                }))
            };
        },

        getWindowState: function() {
            return {
                active: SceneManager._scene ? SceneManager._scene._windowLayer : null,
                windows: SceneManager._scene ? SceneManager._scene._windowLayer.children.length : 0
            };
        }
    };

    // Auto-init when scene is ready
    const original_onMapLoaded = SceneManager.onMapLoaded;
    SceneManager.onMapLoaded = function() {
        original_onMapLoaded.call(this);
        if (window.PLAB) {
            window.PLAB.init();
        }
    };

    // Console commands
    if (debugMode) {
        console.log("PLAB Debug Plugin loaded");
        console.log("Available commands:");
        console.log("  PLAB.getState()");
        console.log("  PLAB.getMapEvents()");
        console.log("  PLAB.getItems()");
        console.log("  PLAB.getWeapons()");
        console.log("  PLAB.getArmor()");
        console.log("  PLAB.getActors()");
        console.log("  PLAB.getPlayerPosition()");
        console.log("  PLAB.getSwitch(id)");
        console.log("  PLAB.setSwitch(id, value)");
        console.log("  PLAB.getVariable(id)");
        console.log("  PLAB.setVariable(id, value)");
        console.log("  PLAB.getGold()");
        console.log("  PLAB.setGold(amount)");
        console.log("  PLAB.addItem(itemId, quantity)");
        console.log("  PLAB.removeItem(itemId, quantity)");
        console.log("  PLAB.teleport(mapId, x, y)");
        console.log("  PLAB.saveGame(slotId)");
        console.log("  PLAB.loadGame(slotId)");
        console.log("  PLAB.getSaveSlots()");
        console.log("  PLAB.getBattleState()");
        console.log("  PLAB.getWindowState()");
    }
})();
```

### Option 2: NW.js DevTools

RPG Maker MV/MZ uses NW.js (Chromium + Node.js). Access DevTools:

```javascript
// In game directory
nw.exe .

// Or with remote debugging
nw.exe . --remote-debugging-port=9222

// Then connect Chrome DevTools to localhost:9222
```

### Option 3: Browser Mode

Some RPG Maker games can run in browser:

```bash
# Serve www/ directory
python -m http.server 8000 --directory www

# Access http://localhost:8000
# Open DevTools (F12)
```

### Option 4: Save File Analysis

RPG Maker saves are JSON files:

```javascript
// Save file location
// Windows: %APPDATA%\<GameName>\save*.json
// macOS: ~/Library/Application Support/<GameName>/save*.json
// Linux: ~/.config/<GameName>/save*.json

// Read save file
const fs = require('fs');
const saveData = JSON.parse(fs.readFileSync('save1.json', 'utf8'));

// Analyze structure
console.log("Map ID:", saveData.mapId);
console.log("Player X:", saveData.player.x);
console.log("Player Y:", saveData.player.y);
console.log("Gold:", saveData.party.gold);
console.log("Items:", saveData.party.items.length);
```

## Key APIs

### Game State

```javascript
// Map
$gameMap.mapId()          // Current map ID
$gameMap.displayName()    // Map name
$gameMap.events()         // All events on map
$gameMap.width()          // Map width
$gameMap.height()         // Map height

// Player
$gamePlayer.x             // Player X position
$gamePlayer.y             // Player Y position
$gamePlayer.direction()   // Facing direction (2=down, 4=left, 6=right, 8=up)
$gamePlayer.isMoving()    // Is player moving?
$gamePlayer.screenX()     // Screen X position
$gamePlayer.screenY()     // Screen Y position

// Party
$gameParty.gold()         // Gold amount
$gameParty.items()        // All items
$gameParty.weapons()      // All weapons
$gameParty.armors()       // All armor
$gameParty.members()      // Party members
$gameParty.leader()       // Party leader

// Switches & Variables
$gameSwitches.value(id)   // Get switch value
$gameSwitches.setValue(id, value)  // Set switch
$gameVariables.value(id)  // Get variable
$gameVariables.setValue(id, value) // Set variable

// Timer
$gameTimer._frames         // Timer frames remaining
$gameTimer._working        // Is timer running?
```

### Data Access

```javascript
// Items
$dataItems[id]            // Item data
item.name                 // Item name
item.price                // Item price
item.consumable           // Is consumable?
item.effects              // Item effects

// Weapons
$dataWeapons[id]          // Weapon data
weapon.name               // Weapon name
weapon.params[2]          // Weapon attack
weapon.price              // Weapon price

// Armor
$dataArmors[id]           // Armor data
armor.name                // Armor name
armor.params[1]           // Armor defense
armor.price               // Armor price

// Actors
$dataActors[id]           // Actor data
actor.name                // Actor name
actor.params[0]           // Max HP
actor.params[1]           // Max MP
actor.params[2]           // Attack
actor.params[3]           // Defense
actor.params[4]           // Magic Attack
actor.params[5]           // Magic Defense
actor.params[6]           // Agility
actor.params[7]           // Luck

// Enemies
$dataEnemies[id]          // Enemy data
enemy.name                // Enemy name
enemy.params[0]           // Max HP
enemy.params[1]           // Max MP

// Skills
$dataSkills[id]           // Skill data
skill.name                // Skill name
skill.mpCost              // MP cost
skill.power               // Skill power
skill.effects             // Skill effects
```

### Event System

```javascript
// Event commands
// $gameTemp.reserveCommonEvent(id)  // Reserve common event
// $gameTemp.reserveAnimation([x, y, id])  // Play animation
// $gameTemp.requestMapLock()        // Lock map
// $gameTemp.requestMapUnlock()      // Unlock map

// Scene manager
SceneManager.goto(Scene_Map)       // Go to map scene
SceneManager.goto(Scene_Battle)    // Go to battle scene
SceneManager.goto(Scene_Menu)      // Go to menu scene
SceneManager.goto(Scene_Gameover)  // Go to game over

// Window layer
$gameMessage.add(text)             // Add message
$gameMessage.isBusy()              // Is message busy?
$gameMessage.clear()               // Clear message
```

### Battle System

```javascript
// Battle state
$gameTroop.members()               // Enemy members
$gameTroop.isEscaped()             // Has player escaped?
$gameTroop.turnCount()             // Current turn count

// Enemy
enemy.enemyId()                    // Enemy ID
enemy.name()                       // Enemy name
enemy.hp                           // Enemy HP
enemy.mp                           // Enemy MP
enemy.isAlive()                    // Is enemy alive?
enemy.isDying()                    // Is enemy dying?

// Actor in battle
actor.hp                           // Actor HP
actor.mp                           // Actor MP
actor.isAlive()                    // Is actor alive?
actor.isDying()                    // Is actor dying?
actor.isInputting()                // Is actor inputting?
actor.isSelecting()                // Is actor selecting?
actor.isForcedAction()             // Is actor forced action?
```

## Input Simulation

### Keyboard Input

```javascript
// Simulate key press
Input.keyMapper.virtualKeyDown(87);  // W key
Input.keyMapper.virtualKeyUp(87);

// Simulate key press via event
const event = new KeyboardEvent('keydown', { keyCode: 87 });
document.dispatchEvent(event);
```

### Touch Input (Mobile)

```javascript
// Simulate touch
touchInput.simulateTouch(0, 100, 100);  // Touch at (100, 100)
touchInput.simulateTouchEnd(0);
```

## Common Defect Catalog

### Critical (P0/P1)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Game won't start | Black screen, no response | Missing plugin, JS error | Check console, fix plugin |
| Save corruption | Crash on load | Data format error, version mismatch | Check save file, verify data |
| Event not triggering | Nothing happens on interaction | Event page condition wrong, command missing | Check event conditions, verify commands |
| Battle crash | Game exits during battle | Enemy data missing, skill error | Check enemy/skill data |
| Infinite loop | Game freezes | Event command loop without exit | Check event commands, add break |

### Major (P2)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Message not showing | Text doesn't appear | Message window not opening, text empty | Check message commands, verify text |
| Movement blocked | Can't walk | Collision tile wrong, event blocking | Check tileset, fix collision |
| Item not working | Item doesn't do anything | Item effect missing, command wrong | Check item data, verify effect |
| Skill not working | Skill doesn't cast | MP cost too high, state missing | Check skill data, verify MP |
| Shop not working | Can't buy/sell | Shop processing missing, price wrong | Check shop event, verify processing |

### Minor (P3/P4)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Text overflow | Text goes off screen | Window size too small, text too long | Increase window size, shorten text |
| Animation missing | No animation plays | Animation ID wrong, file missing | Check animation ID, verify file |
| Sound missing | No sound plays | SE/BGM file missing, volume 0 | Check audio files, verify volume |
| Picture not showing | Image doesn't appear | Picture ID wrong, file missing | Check picture ID, verify file |
| Weather not working | No weather effect | Weather type wrong, region missing | Check weather settings, verify region |

## Save File Analysis

RPG Maker save files are JSON:

```json
{
  "system": { "_switches": [], "_variables": [], "_savefileId": 1 },
  "screen": { "_brightness": 255 },
  "timer": { "_frames": 0, "_working": false },
  "message": { "_texts": [], "_choices": [] },
  "scene": { "_mapId": 1, "_encounterCounter": 0 },
  "map": { "_mapId": 1, "_events": [], "_displayName": "Map Name" },
  "player": { "_x": 10, "_y": 5, "_direction": 2 },
  "party": {
    "_gold": 1000,
    "_items": [{ "id": 1, "amount": 5 }],
    "_weapons": [{ "id": 1, "etouchId": 0 }],
    "_armors": [{ "id": 1, "etouchId": 0 }],
    "_members": [1, 4, 7]
  },
  "actors": [
    {
      "_actorId": 1,
      "_name": "Hero",
      "_nickname": "",
      "_classId": 1,
      "_level": 5,
      "_exp": { "1": 0, "2": 100, "3": 500 },
      "_hp": 100,
      "_mp": 50,
      "_paramPlus": [0, 0, 0, 0, 0, 0, 0, 0],
      "_stateId": [],
      "_stateCounter": {}
    }
  ]
}
```

## Event Command Reference

Common event commands and their IDs:

| Command | ID | Description |
|---|---|---|
| Show Text | 101 | Display message |
| Show Choices | 102 | Display choice menu |
| Input Number | 103 | Get number input |
| Select Key Item | 104 | Select key item |
| Show Scrolling Text | 105 | Scroll text |
| Show Picture | 231 | Display picture |
| Erase Picture | 232 | Remove picture |
| Move Picture | 233 | Move picture |
| Tint Screen | 223 | Change screen tint |
| Flash Screen | 224 | Flash screen |
| Shake Screen | 225 | Shake screen |
| Weather Effect | 236 | Change weather |
| Show Animation | 261 | Play animation |
| Show Balloon Icon | 265 | Show balloon icon |
| Fadeout Screen | 221 | Fade to black |
| Fadein Screen | 222 | Fade from black |
| Tint Picture | 229 | Tint picture |
| Move Event | 230 | Move event |
| Wait | 230 | Wait for time |
| Comment | 108 | Comment (no effect) |
| Conditional Branch | 111 | If/else branch |
| Loop | 112 | Start loop |
| Break Loop | 113 | Break loop |
| Exit Event Processing | 115 | Exit event |
| Erase Event | 116 | Erase event |
| Call Common Event | 117 | Call common event |
| Label | 118 | Label for jump |
| Jump to Label | 119 | Jump to label |
| Control Switches | 121 | Control switches |
| Control Variables | 122 | Control variables |
| Control Self Switch | 123 | Control self switch |
| Control Timer | 124 | Control timer |
| Change Gold | 125 | Change gold |
| Change Items | 126 | Change items |
| Change Weapons | 127 | Change weapons |
| Change Armor | 128 | Change armor |
| Change Party Member | 129 | Change party member |
| Change HP | 356 | Change HP |
| Change MP | 357 | Change MP |
| Change State | 358 | Change state |
| Recover All | 359 | Recover all |
| Change EXP | 320 | Change EXP |
| Change Level | 321 | Change level |
| Change Parameters | 322 | Change parameters |
| Change Skills | 323 | Change skills |
| Change Equipment | 326 | Change equipment |
| Change Name | 324 | Change name |
| Change Class | 325 | Change class |
| Change Actor Images | 327 | Change actor images |
| Change Vehicle Image | 328 | Change vehicle image |
| Change Parallax | 355 | Change parallax |
| Change Map Name Display | 275 | Change map name display |
| Change Tileset | 355 | Change tileset |
| Change Battle BGM | 132 | Change battle BGM |
| Change Victory ME | 133 | Change victory ME |
| Change Save Access | 134 | Change save access |
| Change Menu Access | 135 | Change menu access |
| Change Encounter | 136 | Change encounter |
| Change Formation | 137 | Change formation |
| Change Window Color | 138 | Change window color |
| Change Actors HP | 318 | Change actors HP |
| Change Actors MP | 319 | Change actors MP |
| Change Enemy HP | 331 | Change enemy HP |
| Change Enemy MP | 332 | Change enemy MP |
| Enemy Transform | 339 | Enemy transform |
| Show Battle Animation | 340 | Show battle animation |
| Force Action | 337 | Force action |
| Abort Battle | 335 | Abort battle |
| Open Shop | 302 | Open shop |
| Change Name | 324 | Change name |
| Input Processing | 355 | Input processing |
| Transfer Player | 201 | Transfer player |
| Set Vehicle Location | 202 | Set vehicle location |
| Set Event Location | 203 | Set event location |
| Scroll Map | 204 | Scroll map |
| Set Movement Route | 205 | Set movement route |
| Get On/Off Vehicle | 206 | Get on/off vehicle |
| Show Animation | 207 | Show animation |
| Balloon Icon | 208 | Balloon icon |
| Erase Event | 209 | Erase event |
| Authorize Transaction | 355 | Authorize transaction |
| Prepare Transition | 355 | Prepare transition |
| Execute Transition | 355 | Execute transition |
| Change Player Images | 355 | Change player images |
| Change Transparency | 355 | Change transparency |
| Change Player Merge | 355 | Change player merge |
| Change UI | 355 | Change UI |
| Window Skin | 355 | Window skin |
| Change System Graphics | 355 | Change system graphics |
| Change Battle Back | 355 | Change battle back |
| Enemy Appear | 336 | Enemy appear |
| Change Enemy Traits | 338 | Change enemy traits |
| Change Drop Item | 340 | Change drop item |
| Control Event | 355 | Control event |

## Capability Honesty

What you CAN observe with RPG Maker:

- ✅ Game state (map, player, party, items, gold)
- ✅ Event commands and their execution
- ✅ Save file contents
- ✅ Battle state, enemy data
- ✅ Switches and variables
- ✅ Window/message state
- ✅ Console output (if debug enabled)

What you CANNOT observe without source:

- ❌ Event command internals (unless decompiled)
- ❌ Plugin internals (unless source available)
- ❌ Network internals (unless intercepted)
- ❌ Anti-cheat state (if present)

Document limitations in audit report.
