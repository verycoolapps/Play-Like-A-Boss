# UNREAL ENGINE ADAPTER

Instrumentation and defect catalog for Unreal Engine 4/5 games.

## Detection

Confirm Unreal Engine usage:

```bash
# File system signals
find . -name "*.uproject" -o -name "*.uplugin" -o -name "*.uasset" -o -name "*.umap"
find . -name "Binaries" -type d -o -name "Content" -type d

# Binary signals
file game.exe  # Unreal games have UnrealEditor or packaged binaries
ls -la Binaries/Win64/*.dll  # UnrealEngine.dll, etc.
```

```cpp
// Code signals
#include "GameFramework/Actor.h"
UCLASS()
class AMyActor : public AActor { };
```

```javascript
// Runtime signals
// Unreal games log to:
// Windows: %LOCALAPPDATA%\UnrealEngine\<ProjectName>\Saved\Logs\
// macOS: ~/Library/Logs/Unreal Engine/<ProjectName>/
// Linux: ~/.config/Epic/<ProjectName>/Saved/Logs/
```

## Instrumentation Options

### Option 1: Unreal Editor (PIE - Play In Editor)

If you have the Unreal project source:

```cpp
// Create a Blueprint or C++ actor for automated testing
UCLASS()
class AAutomatedPlaytest : public AActor
{
    GENERATED_BODY()
public:
    virtual void BeginPlay() override
    {
        Super::BeginPlay();
        
        // Run automated test sequence
        RunTestSequence();
    }
    
    void RunTestSequence()
    {
        // Test 1: Player movement
        TestPlayerMovement();
        
        // Test 2: Game state transitions
        TestGameStates();
        
        // Test 3: UI interactions
        TestUI();
    }
};
```

**Advantages**: Full access to actors, components, Blueprint logic.
**Disadvantages**: Requires Unreal Editor, slower than packaged build.

### Option 2: Unreal Automation Framework

```cpp
// Functional test
IMPLEMENT_SIMPLE_AUTOMATION_TEST(FPlayerMovementTest, "MyGame.Player.Movement", EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)

bool FPlayerMovementTest::RunTest(const FString& Parameters)
{
    // Spawn player
    UWorld* World = GEditor->GetEditorWorldContext().World();
    AActor* Player = World->SpawnActor<APlayerStart>();
    
    // Simulate input
    APlayerController* PC = World->GetFirstPlayerController();
    PC->InputKey(FKey("W"), IE_Pressed);
    
    // Wait and verify
    FPlatformProcess::Sleep(0.5f);
    FVector Pos = Player->GetActorLocation();
    TestTrue("Player moved", Pos.Z > 0);
    
    return true;
}
```

Run via: `UnrealEditor.exe Project.uproject -ExecCmds="Automation RunTests MyGame" -unattended -nop4 -nullrhi`

### Option 3: Unreal Insights (Profiler)

For packaged builds:

```bash
# Windows
Game.exe -trace=default -tracehost=127.0.0.1

# macOS
./Game.app/Contents/MacOS/Game -trace=default

# Linux
./Game.x86_64 -trace=default
```

Connect Unreal Insights to analyze:
- CPU usage per frame
- Memory allocations
- Draw calls
- Physics performance
- Network traffic

### Option 4: Unreal Remote Control / HTTP API

If enabled in project settings:

```bash
# Query object properties
curl http://localhost:30010/remote/object/property

# Call functions
curl -X POST http://localhost:30010/remote/object/call
```

### Option 5: Binary Analysis (No Source)

If you only have the packaged game:

```bash
# Check for Unreal version
strings Game.exe | grep -i "unreal"

# Check for pak files
ls *.pak  # Game assets are in pak files

# Use UnrealPak to extract
UnrealPak.exe Game-WindowsNoEditor.pak -extract
```

## Key APIs

### Actor & Component

```cpp
// Spawn actor
AActor* Actor = World->SpawnActor<AActor>(ActorClass, Location, Rotation);

// Get component
UStaticMeshComponent* Mesh = Actor->FindComponentByClass<UStaticMeshComponent>();

// Set properties
Actor->SetActorLocation(FVector(0, 100, 0));
Actor->SetActorRotation(FRotator(0, 90, 0));

// Destroy actor
Actor->Destroy();
```

### Pawn & Controller

```cpp
// Player controller
APlayerController* PC = GetWorld()->GetFirstPlayerController();
APawn* Pawn = PC->GetPawn();

// Input
PC->InputKey(FKey("W"), IE_Pressed);
PC->InputAxis(FKey("MoveForward"), 1.0f);

// Camera
APlayerCameraManager* Camera = PC->PlayerCameraManager;
FVector CamLoc = Camera->GetCameraLocation();
FRotator CamRot = Camera->GetCameraRotation();
```

### Physics

```cpp
// Line trace
FHitResult Hit;
FCollisionQueryParams Params;
bool bHit = GetWorld()->LineTraceSingleByChannel(Hit, Start, End, ECC_Visibility, Params);

// Overlap
TArray<AActor*> OverlappingActors;
GetOverlappingActors(OverlappingActors);

// Physics body
UPrimitiveComponent* PrimComp = GetRootComponent()->GetBodyInstance();
FVector Velocity = PrimComp->GetPhysicsLinearVelocity();
```

### Animation

```cpp
// Skeletal mesh
USkeletalMeshComponent* SkelMesh = GetComponent<USkeletalMeshComponent>();
UAnimInstance* AnimInstance = SkelMesh->GetAnimInstance();

// Play animation
AnimInstance->Montage_Play(AttackMontage);

// Blend space
AnimInstance->SetFloat("Speed", CurrentSpeed);
```

### UI (UMG)

```cpp
// Widget
UUserWidget* Widget = CreateWidget<UUserWidget>(GetWorld(), WidgetClass);
Widget->AddToViewport();

// Button
UButton* Button = Widget->GetButton("StartButton");
Button->OnClicked.AddDynamic(this, &AMyActor::OnStartClicked);

// Text
UTextBlock* Text = Widget->GetText("ScoreText");
Text->SetText(FText::FromString("Score: 100"));
```

### Save/Game State

```cpp
// Save game
USaveGame* SaveGameInstance = UGameplayStatics::CreateSaveGameObject(USaveGame::StaticClass());
UGameplayStatics::SaveGameToSlot(SaveGameInstance, "SaveSlot", 0);

// Load game
USaveGame* LoadedGame = UGameplayStatics::LoadGameFromSlot("SaveSlot", 0);
```

## Input Simulation

### Enhanced Input (UE5)

```cpp
// Input action
UInputAction* MoveAction;
FInputActionValue Value = MoveAction->GetValue();
FVector2D MoveInput = Value.Get<FVector2D>();

// Input mapping context
UInputMappingContext* MappingContext;
MappingContext->MapKey(MoveAction, EKeys::W);
```

### Legacy Input

```cpp
// Axis input
float Forward = GetInputAxisValue("MoveForward");
float Right = GetInputAxisValue("MoveRight");

// Action input
bool bJump = WasInputKeyJustPressed(EKeys::SpaceBar);
```

## Common Defect Catalog

### Critical (P0/P1)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Crash on launch | Game exits immediately | Missing asset, corrupted pak | Verify assets, check logs |
| Infinite loop | Game freezes | While loop without exit, delegate never cleared | Add break conditions, clear delegates |
| Save corruption | Crash on load | Serialization error, version mismatch | Add version check, migration |
| Physics explosion | Objects fly everywhere | NaN values, extreme forces | Validate inputs, clamp forces |
| Null pointer | Crash on play | Missing reference, destroyed actor | Add null checks, fix references |

### Major (P2)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Animation not playing | Static character | Montage not loaded, blend space wrong | Check references, verify assets |
| UI not updating | Score not changing | Widget not bound, event not firing | Check bindings, verify events |
| Collision missing | Objects pass through | Collision preset wrong, channel mismatch | Fix collision settings |
| Audio not playing | No sound | Sound cue not assigned, attenuation wrong | Check references, verify audio |
| AI stuck | NPC stops moving | Pathfinding failure, state machine stuck | Check navmesh, debug AI |

### Minor (P3/P4)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Draw call spam | Low FPS | Too many actors, no instancing | Use HISM, merge actors |
| Memory leak | FPS degrades | Actors not destroyed, delegates not cleared | Call `Destroy()`, clear delegates |
| Texture streaming | Stutter on texture load | Texture pool too small | Increase pool size, preload |
| Shadow acne | Striped shadows | Shadow bias too low | Increase `ShadowBias` |
| LOD issues | Pop-in/pop-out | LOD distances wrong | Adjust LOD settings |

## Log Analysis

Unreal logs to:

- **Windows**: `%LOCALAPPDATA%\UnrealEngine\<ProjectName>\Saved\Logs\`
- **macOS**: `~/Library/Logs/Unreal Engine/<ProjectName>/`
- **Linux**: `~/.config/Epic/<ProjectName>/Saved/Logs/`

```bash
# Tail the log
tail -f ~/Library/Logs/Unreal\ Engine/MyGame/Saved/Logs/MyGame.log

# Search for errors
grep -i "error\|warning\|crash" ~/Library/Logs/Unreal\ Engine/MyGame/Saved/Logs/MyGame.log

# Search for specific actor
grep "MyActor" ~/Library/Logs/Unreal\ Engine/MyGame/Saved/Logs/MyGame.log
```

## Console Commands

Unreal has a built-in console:

```cpp
// Open console with ~ key or F1
// Common commands:

stat fps              // Show FPS
stat unit              // Show draw calls
stat memory            // Show memory usage
stat scenerendering    // Rendering stats

obj list              // List all objects
obj refs <name>       // Find references to object

show collision        // Show collision geometry
show flags            // Show actor flags

quit                  // Quit game
```

## Development Build Flags
n
```bash
# Windows
Game.exe -log -stdout -FullStdOutLogOutput

# With debug
Game.exe -debug -development

# With automation
Game.exe -ExecCmds="Automation RunTests" -unattended -nop4 -nullrhi
```

## When Source Unavailable

If you only have the packaged game:

1. **Extract pak files**: Use UnrealPak to extract assets.
2. **Check logs**: Always check `Saved/Logs/` for errors.
3. **Use console**: If console is enabled, use it for debugging.
4. **Remote control**: If HTTP API is enabled, query object state.
5. **Limitations**: Cannot modify code, only observe behavior.

## Capability Honesty

What you CAN observe with Unreal:

- ✅ Actor hierarchy, components, properties
- ✅ Transform, physics, animation state
- ✅ UI elements, input events
- ✅ Console logs, errors, warnings
- ✅ Profiler data (CPU, memory, draw calls)
- ✅ Asset references, Blueprint structure

What you CANNOT observe without source:

- ❌ Blueprint logic internals (unless decompiled)
- ❌ C++ code behavior (unless decompiled)
- ❌ Network internals (unless intercepted)
- ❌ Editor-only features (unless in development build)

Document limitations in audit report.
