# Template Project Modernization Plan

> 🚀 Strategic roadmap for keeping this template aligned with modern research software development practices

This document outlines planned improvements to keep the template current with best practices in scientific Python development, based on analysis of [AMOCcommunity/amocatlas](https://github.com/AMOCcommunity/amocatlas) and broader research software engineering standards.

## 🔧 **Critical Configuration Updates**

### **1. pyproject.toml Enhancements**
**Current gaps vs. amocatlas:**
- Missing package data specification 
- Lacking tool-specific configurations for ruff and black
- No optional dependencies groups
- Missing author vs maintainer distinction

**Recommended changes:**
- Add `[tool.setuptools.package-data]` section for metadata files
- Expand `[tool.ruff]` configuration with specific rule sets
- Add `[tool.black]` configuration consistency 
- Include `[project.optional-dependencies]` for dev, docs, test groups
- Upgrade setuptools requirement to `>=68` (2024 standard)

### **2. Pre-commit Configuration Updates** *(Lower Priority)*
**Current status:** Basic pre-commit setup works well for most users

**Optional improvements (for advanced users):**
- Update to latest hook versions when needed
- Consider mypy for type checking (adds complexity)
- Note: Pre-commit hooks can be overwhelming for beginners - current setup is intentionally simple

## 🗂 **GitHub Repository Structure**

### **3. Missing Community Health Files**
**Current state:** Basic ISSUE_TEMPLATE.md and PULL_REQUEST_TEMPLATE.md exist but need updates

**Required additions:**
- `CODE_OF_CONDUCT.md` - Research community behavioral standards
- `SECURITY.md` - Vulnerability reporting procedures
- `SUPPORT.md` - Community support channels
- Enhanced issue templates with proper YAML frontmatter

### **4. GitHub Templates Modernization**
**Issues found:**
- Current issue template references "amocarray" instead of template project
- PR template lacks the structured format from amocatlas
- Missing multiple issue templates for bugs vs features

**Updates needed:**
- Fix template references and branding
- Adopt amocatlas PR title conventions (`[DOC]`, `[FIX]`, `[FEAT]`, etc.)
- Add separate issue templates for different types

## 📦 **Package Structure & Organization**

### **5. Module Architecture**
**Current:** Basic template_project package
**amocatlas pattern:** Modular reader architecture with specialized components

**Enhancements:**
- Add proper `__init__.py` with version and main imports
- Include example metadata directory structure
- Add specialized module templates (readers, plotters, tools)
- Include logging configuration as standard

### **6. Testing & Quality Assurance**
**Missing elements:**
- Type hints throughout codebase
- Comprehensive pytest configuration in pyproject.toml
- Coverage reporting setup
- Integration testing examples

## 📚 **Documentation Improvements**

### **7. Documentation Structure**
**Current:** Good Sphinx setup but could be enhanced
**Needed additions:**
- API documentation generation setup
- Example notebooks integration
- Contributing guidelines in docs
- Research software citation guidelines

### **8. Educational Content**
**Gaps identified:**
- No guidance on research data management
- Missing sections on reproducibility
- Limited coverage of scientific Python ecosystem integration

## 🔄 **Workflow & Automation**

### **9. GitHub Actions Enhancement**
**Already improved:** Micromamba integration complete ✅
**Additional opportunities:**
- Add dependency update automation (dependabot)
- Include automated testing matrix for multiple OS/Python versions
- Add draft release automation
- Include security scanning workflows

### **10. Development Workflow**
**Missing features:**
- Automated changelog generation (towncrier)
- Version bumping automation
- Pre-release testing workflows

## 🎯 **Implementation Status & Priority**

### **Phase 1: Critical Infrastructure** 
- [ ] Update pyproject.toml with modern configuration
- [ ] Add missing community health files
- [ ] Fix GitHub template references
- [ ] Pre-commit updates *(optional/advanced)*

### **Phase 2: Package Modernization**
- [ ] Enhance module structure with proper __init__.py
- [ ] Add type hints and improve code quality
- [ ] Update testing configuration
- [ ] Add metadata handling examples

### **Phase 3: Documentation & Workflows**
- [ ] Enhance documentation structure
- [ ] Add research software specific guides
- [ ] Implement additional GitHub Actions
- [ ] Create migration guide for existing projects

## ✅ **Completed Improvements**

- [x] Added GitHub oceanographic tags guide
- [x] Updated requirements structure (-r requirements.txt pattern)
- [x] Added conda/mamba environment support (environment.yml)
- [x] Modernized docs workflows to use micromamba
- [x] Added comprehensive resource links to CLAUDE.md

## 📊 **Success Metrics**

- **Compatibility:** Template works with Python 3.9-3.12
- **Quality:** All pre-commit hooks pass, 90%+ test coverage
- **Usability:** Clear migration path from old to new template
- **Community:** Follows all GitHub community health file standards
- **Research-focused:** Includes discipline-specific best practices for oceanographic research

## 🔗 **References**

This plan is informed by:
- [AMOCcommunity/amocatlas](https://github.com/AMOCcommunity/amocatlas) - Reference implementation
- [Scientific Python Development Guide](https://learn.scientific-python.org/development/)
- [PyOpenSci Python Package Guide](https://www.pyopensci.org/python-package-guide/)
- [GitHub Community Health Files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions)

---

**Last Updated:** October 2024  
**Next Review:** January 2025