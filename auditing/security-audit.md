# SECURITY AUDIT

Authorization-bounded security assessment of game systems: input validation, save file integrity, anti-cheat, network security, and data protection.

## Authorization Boundaries

**CRITICAL**: Security audit operates within strict authorization limits:

- ✅ Test only games you own or have explicit permission to test.
- ✅ Test on local/dev builds, not production servers.
- ✅ No exploitation of live services or real player data.
- ✅ No credential attacks, social engineering, or physical access.
- ✅ No data exfiltration or persistence mechanisms.
- ✅ Document all findings responsibly.

**If authorization is unclear, do not proceed. Ask the user for explicit permission.**

## Audit Scope

Security audit covers:

- Input validation (user input sanitization)
- Save file integrity (tampering, corruption)
- Anti-cheat mechanisms (detection, bypass)
- Network security (man-in-the-middle, packet injection)
- Data protection (encryption, privacy)
- API security (if game has backend)
- Platform security (OS-level vulnerabilities)

## Methodology

For each security element:

1. **Identify** — what security mechanism should exist?
2. **Test** — attempt to bypass or exploit.
3. **Observe** — capture the result.
4. **Verify** — confirm vulnerability or security.
5. **Document** — record finding with responsible disclosure.

## Input Validation

### User Input Sanitization

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| SQL injection | Enter SQL in name/chat field | Input rejected or sanitized | Input log, response |
| XSS injection | Enter script in chat/username | Input sanitized or escaped | Rendered output |
| Buffer overflow | Enter extremely long string | Input truncated or rejected | Input handling |
| Format string | Enter format specifiers | Input treated as literal | Output verification |
| Command injection | Enter shell commands | Input rejected or sanitized | System logs |

### Game Input Validation

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Invalid item ID | Use non-existent item | Item rejected or handled | Inventory state |
| Invalid weapon ID | Equip non-existent weapon | Weapon rejected | Equipment state |
| Invalid map ID | Teleport to non-existent map | Teleport rejected | Map state |
| Invalid coordinates | Move to invalid position | Position clamped or rejected | Position state |
| Negative values | Enter negative health/gold | Values clamped or rejected | State verification |

## Save File Integrity

### Tampering Detection

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Modify save file | Edit save file values | Game detects tampering | Error message, reset |
| Delete save file | Remove save file | Game handles gracefully | Error handling |
| Corrupt save file | Truncate/corrupt save | Game handles gracefully | Error handling |
| Version mismatch | Load old save format | Game migrates or rejects | Migration log |
| Checksum verification | Modify save, keep checksum | Checksum mismatch detected | Checksum verification |

### Save File Security

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Encryption | Check if save is encrypted | Encrypted or obfuscated | File analysis |
| Signing | Check if save is signed | Signed or authenticated | Signature verification |
| Compression | Check if save is compressed | Compressed or readable | File format |
| Backup | Check for backup saves | Automatic backups created | File system check |

## Anti-Cheat

### Detection Mechanisms

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Speed hack | Modify game speed | Detection or correction | Speed verification |
| Memory editing | Edit game memory | Detection or protection | Memory integrity |
| Packet injection | Inject fake packets | Detection or rejection | Network logs |
| Replay attack | Replay old inputs | Detection or rejection | Input validation |
| Wall hack | See through walls | Detection or prevention | Rendering check |

### Bypass Attempts

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Debug mode | Enable debug/cheat mode | Restricted or authenticated | Debug access |
| Console commands | Use console commands | Restricted or authenticated | Command execution |
| Save editing | Edit save file for advantages | Detection or prevention | Save verification |
| Mod injection | Inject mod/cheat code | Detection or prevention | Code integrity |

## Network Security

### Man-in-the-Middle

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| SSL/TLS | Check if connection encrypted | Encrypted connection | Certificate verification |
| Certificate pinning | Check if cert is pinned | Certificate validation | SSL handshake |
| Proxy detection | Check if proxy detected | Proxy detected or blocked | Network logs |
| Packet inspection | Inspect network traffic | Encrypted or secured | Packet capture |

### Packet Injection

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Fake packets | Send invalid packets | Packets rejected | Server logs |
| Replay packets | Replay old packets | Packets rejected | Timestamp validation |
| Packet modification | Modify packet data | Integrity check fails | Checksum verification |
| Flood attack | Send excessive packets | Rate limiting or blocking | Server response |

### Server Authority

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Client trust | Check if client trusted | Server validates | Server logs |
| State sync | Check state synchronization | Server authoritative | State comparison |
| Anti-cheat server | Check server-side anti-cheat | Server-side detection | Server logs |

## Data Protection

### Personal Data

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Data collection | Check what data is collected | Minimal necessary data | Privacy policy, data logs |
| Data storage | Check how data is stored | Encrypted or secure | Storage analysis |
| Data sharing | Check if data is shared | Only with consent | Privacy policy |
| Data deletion | Check if data can be deleted | User can delete data | Deletion test |

### Encryption

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Data encryption | Check if data encrypted | Encrypted at rest | File analysis |
| Transit encryption | Check if data encrypted in transit | TLS/SSL used | Network analysis |
| Key management | Check how keys are managed | Secure key storage | Key analysis |

## API Security (if applicable)

### Authentication

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Authentication bypass | Attempt to bypass auth | Auth required | Access denied |
| Token validation | Check token validation | Tokens validated | Token verification |
| Session management | Check session handling | Secure sessions | Session analysis |

### Authorization

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Privilege escalation | Attempt to gain admin | Privileges enforced | Access denied |
| IDOR | Access other users' data | Authorization checked | Access denied |
| Rate limiting | Check rate limits | Rate limiting enforced | Rate limit response |

## Platform Security

### OS-Level

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| File permissions | Check file permissions | Appropriate permissions | Permission check |
| Process isolation | Check process isolation | Sandboxed or isolated | Process analysis |
| Memory protection | Check memory protection | Protected memory | Memory analysis |

### Mobile Security

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Jailbreak detection | Check if jailbreak detected | Detection or prevention | Jailbreak test |
| Root detection | Check if root detected | Detection or prevention | Root test |
| App sandbox | Check app sandboxing | Sandboxed | Sandbox verification |

## Common Security Bugs

### Critical (P0/P1)

| Bug | Symptom | Impact | Fix |
|---|---|---|---|
| Remote code execution | Attacker can execute code | Complete system compromise | Input validation, sandboxing |
| SQL injection | Database compromised | Data theft, manipulation | Parameterized queries |
| Authentication bypass | Unauthorized access | Account takeover | Strong auth, session management |
| Data breach | Personal data exposed | Privacy violation, legal issues | Encryption, access control |
| Anti-cheat bypass | Cheats undetected | Game integrity compromised | Server-side validation |

### Major (P2)

| Bug | Symptom | Impact | Fix |
|---|---|---|---|
| Input validation | Invalid input accepted | Game logic bypass | Input sanitization |
| Save tampering | Save file editable | Cheat advantage | Save signing, encryption |
| Network sniffing | Unencrypted traffic | Data interception | TLS/SSL encryption |
| Session hijacking | Session stolen | Account takeover | Secure session management |
| Privilege escalation | User gains admin | Unauthorized access | Proper authorization |

### Minor (P3/P4)

| Bug | Symptom | Impact | Fix |
|---|---|---|---|
| Information disclosure | Sensitive info exposed | Privacy concern | Remove debug info |
| Weak encryption | Easily broken encryption | Data exposure | Stronger encryption |
| Missing rate limit | DoS possible | Service disruption | Rate limiting |
| Poor logging | Security events not logged | Delayed detection | Comprehensive logging |
| Outdated dependencies | Known vulnerabilities | Security risk | Update dependencies |

## Evidence Collection

For each security test:

1. **Setup** — describe security test scenario.
2. **Attack** — what was attempted.
3. **Result** — what happened.
4. **Evidence** — logs, screenshots, packet captures.
5. **Impact** — potential damage.
6. **Recommendation** — how to fix.

Store evidence in `.plab/session-*/evidence/security/`.

## Responsible Disclosure

If you find a security vulnerability:

1. **Document** — record the vulnerability with evidence.
2. **Assess** — determine severity and impact.
3. **Notify** — inform the game developer/owner.
4. **Allow time** — give reasonable time for fix.
5. **Verify** — confirm fix is deployed.
6. **Publish** — disclose responsibly after fix.

**Never exploit vulnerabilities for personal gain. Never publicly disclose before fix is deployed.**

## When to Stop

Stop security audit when:

- All security elements tested.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted.
- Authorization limits reached.
- Platform limits prevent further testing.

## Integration with Other Audits

Security audit findings may reveal issues in other dimensions:

- Input validation → functional audit
- Network security → performance audit
- Data protection → functional audit
- Anti-cheat → gameplay audit

Cross-reference findings and coordinate audits.
