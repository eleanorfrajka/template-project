# Transferring a Repository to an Organisation

> 🏢 This guide explains how to transfer a GitHub repository from a personal account to an organisation. While not required, this can help promote collaborative ownership and reduce barriers to contribution.

---

## 📦 Why Transfer to an Organisation?

- Enables team-based permissions
- Reduces visibility of individual ownership
- Simplifies future collaboration and maintenance

You might want to transfer if you're planning broader community involvement, long-term support, or a publication release.

---

## 🔁 Steps for Transferring a Repository

### 1. Prepare an Organisation and Team
- Make sure you're an admin of the destination GitHub organisation.
- Create a team for maintainers (e.g., [`ifmeo-hamburg/seagliderOG1-maintainers`](https://github.com/orgs/ifmeo-hamburg/teams/seagliderOG1-maintainers)).

### 2. Transfer the Repository
- Go to **Settings** in your GitHub repo.
- Scroll to **Danger Zone** and click **Transfer Ownership**.
- Enter the organisation name and confirm.

### 3. Verify the Move
- Go to the new repository URL under the organisation.
- Check that all content moved:
  - Issues
  - Pull requests
  - Branch protection rules

### 4. Reassign Roles
- Visit **Settings > Collaborators and Teams**.
- Ensure team members have appropriate roles (e.g., “Write” or “Maintain”).

### 5. Notify Collaborators
- Let team members and contributors know the repo has moved.

---

## ⚙️ Post-Transfer Clean-up

### 🔗 Update Links
- [ ] Update all internal links to the repo in:
  - `README.md`
  - `docs/index.rst`
  - `docs/source/conf.py`
  - Citation files (e.g. `CITATION.cff` → `url:` field)

### 📄 PyPI and Trusted Publisher (Later Step)
- [ ] In [PyPI settings](https://pypi.org/manage/project/), update the GitHub repository address.
- [ ] Reconfigure trusted publisher settings for the new repo path.

### 🐍 Conda-forge (Later Step)
- [ ] If distributing via conda-forge, update `meta.yaml` to match the new repo location.

### 📝 `pyproject.toml`
- [ ] Update `urls.repository` and `urls.documentation` to the new GitHub URL.

---

## 👤 Final Step for Original Owner

If the repo started under your personal account (e.g., `github.com/eleanorfrajka/seagliderOG1`) and you want to keep working on it:
- Fork the new repo from the organisation to your personal GitHub account.

---

> ✅ After transfer and cleanup, your repository is easier to maintain as a team project and better prepared for citation, publishing, and long-term support.
