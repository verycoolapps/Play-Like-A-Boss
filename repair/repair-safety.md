# REPAIR SAFETY

Safety protocols for game repairs. Ensures repairs don't cause more harm than good.

## Safety Philosophy

**First, do no harm.** A repair that breaks more than it fixes is worse than no repair. Safety protocols prevent catastrophic mistakes.

## Safety Rules

### Rule 1: Never Repair Without Understanding

**Never fix a bug you don't understand.**

- ❌ Don't guess at fixes.
- ❌ Don't copy-paste solutions.
- ❌ Don't apply workarounds without understanding why.
- ✅ Understand root cause first.
- ✅ Verify hypothesis before fixing.
- ✅ Test fix before deploying.

### Rule 2: Always Checkpoint

**Never make changes without a restorable checkpoint.**

- ❌ Don't edit code without git commit/stash.
- ❌ Don't modify files without backup.
- ❌ Don't deploy without rollback plan.
- ✅ Create git branch or tag.
- ✅ Backup files before modification.
- ✅ Document rollback procedure.

### Rule 3: Minimal Changes Only

**Never make unnecessary changes.**

- ❌ Don't refactor unrelated code.
- ❌ Don't reformat unrelated code.
- ❌ Don't rename variables/functions.
- ❌ Don't "improve" code while fixing bugs.
- ✅ Change only what's necessary.
- ✅ Match existing code style.
- ✅ Keep diff minimal.

### Rule 4: Test Before Deploying

**Never deploy untested fixes.**

- ❌ Don't skip testing.
- ❌ Don't assume fix works.
- ❌ Don't deploy to production without staging.
- ✅ Test fix in isolation.
- ✅ Run regression tests.
- ✅ Verify in actual game.
- ✅ Test edge cases.

### Rule 5: Document Everything

**Never make undocumented changes.**

- ❌ Don't make changes without commit message.
- ❌ Don't fix bugs without bug report.
- ❌ Don't deploy without changelog.
- ✅ Write clear commit messages.
- ✅ Document bug and fix.
- ✅ Update changelog.

### Rule 6: Respect Authorization

**Never exceed authorization boundaries.**

- ❌ Don't repair production systems without permission.
- ❌ Don't modify games you don't own.
- ❌ Don't bypass security for convenience.
- ✅ Work within authorized scope.
- ✅ Ask for permission when unclear.
- ✅ Respect platform limitations.

## Checkpoint Strategies

### Git-Based Checkpoints

```bash
# Create branch for repair
git checkout -b fix/PLAB-NNNN-description

# Commit current state (if needed)
git add .
git commit -m "WIP: before PLAB-NNNN fix"

# Create tag for rollback
git tag checkpoint/before-PLAB-NNNN

# After fix, commit
git add .
git commit -m "fix: PLAB-NNNN description"

# If rollback needed
git checkout checkpoint/before-PLAB-NNNN
# or
git reset --hard checkpoint/before-PLAB-NNNN
```

### File-Based Checkpoints

```bash
# Backup files before modification
cp file.js file.js.backup
cp file.js file.js.original

# Or use version control for individual files
# Some editors have local history
```

### Snapshot-Based Checkpoints

```bash
# VM/Container snapshot
# Create snapshot before major changes
# Can revert to snapshot if needed
```

## Risk Assessment

Before repairing, assess risk:

| Risk Level | Criteria | Action |
|---|---|---|
| **Low** | Isolated change, easy to test, easy to revert | Proceed with standard workflow |
| **Medium** | Affects multiple systems, harder to test | Extra testing, careful review |
| **High** | Core system, hard to test, hard to revert | Extensive testing, peer review, staged rollout |
| **Critical** | Production system, irreversible, high impact | Full review, staging, canary deployment, rollback plan |

## Rollback Procedures

### Git Rollback

```bash
# Revert specific commit
git revert <commit-hash>

# Reset to previous commit (destructive)
git reset --hard <commit-hash>

# Checkout previous state
git checkout <commit-hash>

# Restore from tag
git checkout checkpoint/before-PLAB-NNNN
```

### File Rollback

```bash
# Restore from backup
cp file.js.backup file.js

# Or use version control to restore specific file
git checkout <commit> -- file.js
```

### Deployment Rollback

```bash
# Revert deployment
git revert <commit>
git push

# Or redeploy previous version
# Platform-specific rollback procedure
```

## Safety Checklists

### Pre-Repair Checklist

- [ ] Bug understood and reproduced.
- [ ] Root cause identified.
- [ ] Fix designed and reviewed.
- [ ] Checkpoint created.
- [ ] Risk assessed.
- [ ] Test plan created.
- [ ] Rollback plan documented.

### During-Repair Checklist

- [ ] Minimal changes only.
- [ ] Code style consistent.
- [ ] No unrelated changes.
- [ ] Changes tested in isolation.
- [ ] No new warnings/errors.
- [ ] Documentation updated.

### Post-Repair Checklist

- [ ] Fix verified in actual game.
- [ ] Regression tests pass.
- [ ] Edge cases tested.
- [ ] Performance acceptable.
- [ ] Documentation complete.
- [ ] Knowledge base updated.
- [ ] Rollback plan tested.

## Common Safety Mistakes

### Mistake 1: Fixing Symptoms

**Problem**: Fixing the visible symptom without understanding root cause.

**Example**: Adding null check instead of fixing why object is null.

**Solution**: Always do root cause analysis first.

### Mistake 2: Over-Fixing

**Problem**: Making unnecessary changes while fixing a bug.

**Example**: Refactoring code, reformatting, renaming while fixing bug.

**Solution**: Minimal changes only. One concern per commit.

### Mistake 3: Skipping Tests

**Problem**: Deploying fix without testing.

**Example**: "It looks right, let's ship it."

**Solution**: Always test. Always verify. Always regress.

### Mistake 4: Ignoring Edge Cases

**Problem**: Fix works for main case but breaks edge cases.

**Example**: Fix works for positive numbers but breaks for negative.

**Solution**: Test boundary conditions. Test edge cases.

### Mistake 5: No Rollback Plan

**Problem**: Can't revert if fix doesn't work.

**Example**: Made changes without checkpoint, can't undo.

**Solution**: Always checkpoint. Always document rollback.

## Emergency Procedures

### If Repair Breaks Production

1. **Stop** — halt deployment immediately.
2. **Assess** — determine extent of damage.
3. **Rollback** — revert to last known good state.
4. **Communicate** — notify stakeholders.
5. **Analyze** — understand what went wrong.
6. **Fix properly** — address root cause, not symptom.
7. **Test thoroughly** — ensure fix doesn't break again.

### If Repair Causes Data Loss

1. **Stop** — halt all operations.
2. **Assess** — determine what data was lost.
3. **Restore** — recover from backup if available.
4. **Communicate** — notify affected users.
5. **Analyze** — understand root cause.
6. **Fix** — prevent recurrence.
7. **Document** — record incident and lessons learned.

## Safety Metrics

Track safety metrics:

| Metric | Target | Measurement |
|---|---|---|
| Rollback rate | < 5% | Repairs requiring rollback |
| Regression rate | < 5% | Repairs causing new bugs |
| Test coverage | > 80% | Tested code / total code |
| Documentation rate | 100% | Documented repairs / total repairs |

## When Safety Protocols Can Be Relaxed

Safety protocols can be relaxed only when:

- **Emergency hotfix** — production is down, need immediate fix.
- **Trivial change** — typo fix, comment update, documentation.
- **Well-tested change** — change already tested in staging.
- **User explicitly approves** — user understands risks and approves.

**Even when relaxed, never skip:**
- Understanding root cause.
- Creating checkpoint.
- Basic testing.
- Documentation.

## Integration with Other Modules

- **Intelligent repair** → `repair/intelligent-repair.md`
- **Root cause analysis** → `repair/root-cause-analysis.md`
- **Regression testing** → `repair/regression-testing.md`
- **Release validation** → `testing/release-validation.md`
