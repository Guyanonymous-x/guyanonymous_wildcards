# Versioning

- `main` always holds the latest finished version of the library, tools and docs.
- Each version is one commit (or a short run of commits) with the message `vNN: summary`.
- A branch `release/vNN` is pushed at each release so any version can be recovered. (Tags and GitHub releases cannot be created from the Claude session, so branches are used instead. Create a tag locally with `git tag vNN release/vNN` if you want one.)
- Each version's showcase prompts live in `docs/showcase/`.
- v74 is the first version tracked in git. Earlier versions exist only as zips.
