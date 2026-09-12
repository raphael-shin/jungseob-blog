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

원본을 수정하지 않습니다. 본문은 중복된 첫 H1만 제거하며, 출처와 수정일을 보존합니다. 위키 링크와 로컬 첨부는 변환 전에 해결해야 합니다. 전체 노트 폴더를 자동 공개하지 않습니다. 2026년 9월 생성 노트 71편을 명시적으로 선택해 수록했습니다. 기존 게시글의 고정 주소를 유지합니다.

## 배포

main에 push하면 GitHub Actions가 빌드, 내부 링크 검사, GitHub Pages 배포를 실행합니다. Pages의 Source는 GitHub Actions입니다. 게시 후 실제 공개 URL을 확인합니다.

매일 수집 예약 작업과 Hermes 이메일 발송은 별도입니다. 이 저장소만으로 예약 수집이나 이메일 발송을 수행하지 않습니다.

## 테마

[Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)와 [공식 Starter](https://github.com/cotes2020/chirpy-starter)를 기반으로 합니다. 테마와 시작 코드의 MIT 라이선스는 LICENSE에 보존했습니다. 게시글의 원문 출처는 각 글의 Source를 참고하세요.

## 원문 대표 이미지와 한글 폰트

가져오기 도구는 원문의 `og:image`, Twitter 이미지, 대표 썸네일 순으로 접근 가능한 이미지를 찾습니다. 이미지가 있으면 제목 위와 목록 카드에 표시하고, 없으면 생략합니다. 원격 이미지 URL만 참조하며 이미지를 저장소에 복제하지 않습니다. 출처에서 이미지를 삭제하거나 외부 표시를 차단하면 표시되지 않을 수 있습니다.

결과는 `publishing/source-images.json`에 보관합니다. `--refresh-images`로 다시 확인할 수 있습니다. 본문과 원본 노트는 변경하지 않습니다.

한글 폰트는 을유문화사 공식 배포본의 을유1945 Regular/SemiBold이며, `assets/css/jekyll-theme-chirpy.scss`와 `_includes/head.html`에서 바꿀 수 있습니다. 공식 WOFF2 파일을 변경 없이 사용하며, 폰트 로딩 전에는 시스템 명조 글꼴로 표시합니다. 서체의 출처와 별도 이용 조건은 `assets/fonts/eulyoo1945/NOTICE.md`에 보존합니다.
