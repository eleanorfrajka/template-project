You can delete unused sections.

## PR Title Convention

Please prefix your pull request title with one of the following tags for clarity:

- `[DOC]` for documentation updates
- `[FIX]` for bug fixes
- `[FEAT]` for new features
- `[REFACTOR]` for code improvements
- `[TEST]` for tests
- `[CI]` for CI/CD or automation updates
- `[CLEANUP]` for general maintenance

Example:
> `[FEAT] Add PNG map generation for cruise track visualization`

## Summary
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix/feature causing existing functionality to not work)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring (no functional changes)

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing performed (describe scenarios)
- [ ] I have run `pytest` to check that all tests pass
- [ ] I have run `pre-commit run --all-files` to lint and format the code

## Documentation
- [ ] Docstrings updated
- [ ] User documentation updated
- [ ] Examples/tutorials updated if needed
- [ ] I have followed the coding conventions in CONTRIBUTING.md

## Scientific Validation
(For calculation/algorithm changes)
- [ ] Cross-checked with published methods
- [ ] Tested against known reference values
- [ ] Units and coordinate systems validated

## Breaking Changes
List any breaking changes and migration path for users.

## Related Issues
Closes #123, Addresses #456

## Additional Notes
Include any additional information reviewers might need:

- Screenshots (if UI/outputs are affected)
- Design decisions or trade-offs
- Anything reviewers should look at closely