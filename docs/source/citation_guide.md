# How to Cite This Project

> 🧾 This guide explains how to create and maintain a `CITATION.cff` file and how to generate a DOI for your project using Zenodo.

Providing a clear citation file helps others give you credit for your work — and it only takes a few minutes to set up.

---

## 📄 What is `CITATION.cff`?

- A `CITATION.cff` file lives in the root of your GitHub repository.
- It tells others how to cite your project (e.g. in papers, presentations, or other software).
- GitHub automatically detects this file and shows a “Cite this repository” button in the sidebar.

📚 [CFF Format Documentation](https://citation-file-format.github.io/)

---

## ✍️ Example `CITATION.cff`

```yaml
cff-version: 1.2.0
title: Template Project for Research Code
authors:
  - family-names: Frajka-Williams
    given-names: Eleanor
    orcid: https://orcid.org/0000-0002-XXXX-XXXX
    affiliation: University of Hamburg
version: 0.1.0
date-released: 2024-06-01
license: MIT
url: https://github.com/eleanorfrajka/template-project
message: "If you use this template in your own work, please cite it using the metadata above."
```

> 💡 Keep your `CITATION.cff` updated with new versions and release dates when you publish.

---

## 🌐 Linking to a DOI with Zenodo

Zenodo is a service that archives GitHub releases and issues a DOI (Digital Object Identifier) for your project.

### 🧭 Steps to Register with Zenodo:

1. Log in at [zenodo.org](https://zenodo.org/) using your GitHub account.
2. Go to [GitHub Linked Accounts](https://zenodo.org/account/settings/github/)
3. Enable Zenodo archiving for your repository.
4. Push a new GitHub release tag (e.g. `v0.1.0`).
5. Zenodo will archive the release and issue a DOI.

You can then add that DOI back into your `CITATION.cff` like this:
```yaml
doi: 10.5281/zenodo.1234567
```

📚 [Zenodo GitHub Integration Guide](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories-with-zenodo)

---

## 🧩 Best Practices

- Always include a `CITATION.cff` in published repositories.
- Keep `version` and `date-released` in sync with your actual GitHub tags.
- Use ORCID and affiliation fields to improve citation metadata.
- If you create a Zenodo DOI, display it in the README badge or footer.

---

> ✅ Adding a `CITATION.cff` is a simple but powerful step toward making your code citable and FAIR (Findable, Accessible, Interoperable, Reusable).
