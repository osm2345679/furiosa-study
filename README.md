# furiosa-study

Furiosa NPU 환경에서 진행하는 Python / LLM 추론 실습 기록입니다.

## 폴더 구성

- `furiosa01/`: Furiosa LLM 기본 추론, OpenAI 호환 API, LangChain, 스트리밍 실습
- `furiosa02/`: 지연 시간, TPS, 동시 요청, KV / Prefix Cache, 서버 메트릭 실습
- `my/`: 비전 및 감성 분류 실습

## VS Code에서 작업하기

1. Remote - SSH로 `furiosa-npu`에 접속합니다.
2. `/root/furiosa-study` 폴더를 엽니다.
3. 기존 NPU 실습용 Python / Conda 환경을 선택합니다.
4. 소스 제어에서 변경 확인 → 스테이징 → 커밋 → 변경 내용 동기화를 진행합니다.

터미널에서도 동일하게 관리할 수 있습니다.

```bash
cd /root/furiosa-study
git status
git add furiosa01/ furiosa02/ my/
git commit -m "실습 내용 기록"
git push
```

원격 변경을 받을 때는 `git pull --ff-only`를 사용합니다.

## 실행 환경

기존 서버의 Furiosa SDK / NPU 드라이버와 실습용 Conda 환경을 사용합니다.
API 기반 예제는 로컬의 OpenAI 호환 서버(`127.0.0.1:8000`)를 사용합니다.
Furiosa SDK를 직접 호출하는 예제는 사용 가능한 NPU 및 해당 모델이 필요합니다.
`api_key="EMPTY"`는 로컬 서버용 더미 값입니다. 실제 인증 정보는 코드에 저장하지 않습니다.

## Git 관리 범위

실습 코드와 코드 안에 기록한 실험 결과를 관리합니다.
Python 캐시, 가상환경, `.env`, 머신별 VS Code 설정, 다운로드한 데이터,
모델 가중치, `.fxb` 파일, 생성된 로그와 결과 디렉터리는 `.gitignore`로 제외합니다.
`setting.py`는 실습 코드이므로 추적합니다.

GitHub 인증에는 이 저장소 전용 SSH deploy key를 사용합니다.
개인 키는 서버의 `~/.ssh/`에만 보관하며 저장소에 포함하지 않습니다.
