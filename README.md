# 정섭의 지식 노트

Jekyll + Chirpy로 만든 한국어 기술 블로그입니다.

공개 주소: https://raphael-shin.github.io/jungseob-blog/

## 로컬 미리보기

Ruby 3.4를 사용합니다.

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

http://127.0.0.1:4000/jungseob-blog/ 에서 확인합니다.

## 지식 노트 가져오기

원본 Markdown은 저장소 밖에 보관합니다. `publishing/selection.json`에 파일명과 고정 slug를 명시한 글만 가져옵니다. `publish: true`가 필요합니다.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests
.venv/bin/python scripts/import_notes.py --source-dir /path/to/knowledge-notes
JEKYLL_ENV=production bundle exec jekyll build
```

원본을 수정하지 않습니다. 본문은 중복된 첫 H1만 제거하며, 출처와 수정일을 보존합니다. 위키 링크와 로컬 첨부는 변환 전에 해결해야 합니다. 전체 노트 폴더를 자동 공개하지 않습니다. 처음에는 검증한 글 3편만 수록합니다.

## 배포

main에 push하면 GitHub Actions가 빌드, 내부 링크 검사, GitHub Pages 배포를 실행합니다. Pages의 Source는 GitHub Actions입니다. 게시 후 실제 공개 URL을 확인합니다.

매일 수집 예약 작업과 Hermes 이메일 발송은 별도입니다. 이 저장소만으로 예약 수집이나 이메일 발송을 수행하지 않습니다.

## 테마

[Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)와 [공식 Starter](https://github.com/cotes2020/chirpy-starter)를 기반으로 합니다. 테마와 시작 코드의 MIT 라이선스는 LICENSE에 보존했습니다. 게시글의 원문 출처는 각 글의 Source를 참고하세요.
