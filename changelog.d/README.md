# Changelog Fragments

This directory contains "changelog fragments" - small files that describe changes for the automated changelog generation using [towncrier](https://towncrier.readthedocs.io/).

## Usage

### Adding a changelog fragment

When you make a change that should appear in the changelog, create a file in this directory:

```bash
# For a new feature (e.g., issue #123):
echo "Add support for custom data readers" > changelog.d/123.feature.md

# For a bug fix (e.g., issue #124):  
echo "Fix memory leak in data processing pipeline" > changelog.d/124.bugfix.md

# For documentation updates:
echo "Update installation guide with conda instructions" > changelog.d/125.doc.md

# For removal/deprecation:
echo "Deprecate old plotting interface" > changelog.d/126.removal.md

# For miscellaneous changes (won't show content):
echo "Internal refactoring" > changelog.d/127.misc.md
```

### File naming convention

`{issue_number}.{type}.md`

Where `{type}` is one of:
- `feature` - New features and enhancements
- `bugfix` - Bug fixes
- `doc` - Documentation changes
- `removal` - Deprecations and removals  
- `misc` - Miscellaneous internal changes

### Generating the changelog

```bash
# Preview what will be added to CHANGELOG.md:
towncrier build --draft

# Actually build and update CHANGELOG.md:
towncrier build

# Build for a specific version:
towncrier build --version=1.2.0
```

This will:
1. Collect all fragments from this directory
2. Group them by type
3. Add them to `CHANGELOG.md`
4. Remove the fragment files (unless using `--keep`)

### Example workflow

1. **Make changes** and create PR
2. **Add changelog fragment** describing the change
3. **PR gets merged** 
4. **On release**: Run `towncrier build --version=x.y.z`
5. **Commit and tag** the release

## Templates

The changelog uses the template in `_template.md` which formats entries in Markdown compatible with GitHub releases.