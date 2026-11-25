# Blog publishing

Source notes remain outside this repository. Import only files explicitly listed in publishing/selection.json with publish:true. Never scan or copy the entire vault. scripts/import_notes.py preserves the body except the redundant first H1; source author is not the blog author. Dates and stable slugs must survive subsequent imports. Run importer tests and a production Jekyll build before pushing. The daily automation and Hermes mail are separate and must not be changed as part of site work. New local attachments and wiki links must be resolved before importing; fail rather than silently breaking links.

## Cursor Cloud specific instructions

Ruby 3.4 and Bundler 4.0.15 are on `/usr/local/bin`. The environment install sets `bundle config set --local path vendor/bundle`, runs `bundle install`, and creates the importer virtualenv at `/opt/blog-importer`. Do not create `.venv` inside the repository; Jekyll's file watcher reports an error when that directory is present. On boot, `bash tools/run.sh -H 0.0.0.0` serves http://127.0.0.1:4000/jungseob-blog/. If port 4000 is already listening, leave that server running. Importer tests: `/opt/blog-importer/bin/python -m unittest discover -s tests`. Production build and internal link check: `bash tools/test.sh`.
