# Git Hub 사용법(프로젝트)

### 1. 팀장 작업 (레포 및 브랜치 세팅)

1. **레포 만들기 (팀장)**

2. **팀원 초대하기 (팀장)**
   
   - 메인페이지 invite Collaborators 클릭(또는 settings -> collaborators로 이동)
   - 화면 Manage access의 Add people 클릭해서 팀원 추가
   
3. **초대 수락누르기 (팀원)**

   - 메일이나 깃허브 들어가서 수락 누르면 됨

4. **로컬에서 프로젝트 하나 만들기 (팀장)**

   - 프로젝트 생성 후 아래 명령어 실행
   - `git init`
   - `add, commit`
   - `git remote add origin 주소` (레포 주소를 origin이라는 별칭으로 연결하겠다는 의미)
   - `git push origin master` (별칭 origin이라는 레포의 master 브랜치에 업로드 하겠다는 의미)

5. **develop branch(연습장) 만들기 (팀장)**

   - 터미널에 ` git switch -c develop` 입력
     - 명령어를 입력하는 시점에서 사용중인 브랜치를 복사한 develop 브랜치가 생성됨
   -  터미널에 ``git push --set-upstream origin develop`` 입력
     - 로컬의 'develop' 브랜치를 'origin' 레포의  'develop' 브랜치와 연결하고 레포에 업로드하는 것
     - 그냥 `git push`만 입력하면 `git push --set-upstream origin develop` 에러뜸 
       - 로컬에서만 develop 브랜치를 생성했기 때문에 GitHub 레포에는 아직 develop 브랜치가 없어서 발생 
       - `--set-upstream` (또는 `-u`): 현재 브랜치를 원격 브랜치(=레포 브랜치)와 연결. 즉, 추후에 `git push`나 `git pull` 명령어를 사용할 때 매번 원격 브랜치를 명시할 필요가 없게 됨

   > 참고:
   >
   > - 브랜치
   >   - master 브랜치: 최종 결과물이 업로드 되는 브랜치
   >
   >   - develop 브랜치 : 팀 전체 연습장 (최종 결과물 전에 연습장 처럼 사용하는 팀 브랜치)
   >   - feature 브랜치 : 개인이 쓰는 연습장 (devlop 브랜치로 가기 전에 개인이 사용하는 연습장 브랜치)
   >
   > - branch 관련 명령어
   >   - `git branch [브랜치명]`: 새로운 브랜치를 생성
   >   - `git checkout -b [브랜치명]`: 새로운 브랜치 생성하고 바로 그 브랜치로 전환
   >   - `git switch -c [브랜치명]`: 새로운 브랜치 생성하고 바로 그 브랜치로 전환
   >   - 최신 버전의 Git에서는 `git switch`와 `git restore` 명령어가 `git checkout`의 기능을 대체. 이는 `git checkout` 명령어가 여러 기능을 포함하고 있어 사용하기 복잡했기 때문

6. **master 브랜치 보호하기 (팀장)** : 개개인이 master 브랜치를 바꿀수 없도록 잠구는 작업
   
   - GitHub 메인페이지 → master 브랜치 → Protect this Branch 클릭
     - 또는 settings → Code and automation → Branches로 이동
     - Branch name pattern란에 보호할 브랜치명 적기
   - **Require a pull request before merging 권장**
     - 해당 브랜치에 직접 PUSH할 수 없게함. 무조건 PR(Pull Request)을 통해서만 반영할 수 있게 만드는 옵션. 
     - 세부옵션 
       -  Require approvals : PR의 승인할 인원수
   - **Lock Branch 권장 (정확히 무슨 기능인지 못 찾겠어서 추정해서 작성함..)**
     - 해당 브랜치를 읽기 전용으로 바꿔서 읽는거 제외하고 모든 동작 잠궈두는 옵션으로 추정됨..
     - Lock Branch 옵션이 활성화된 Branch에 push, merge 등 다른 작업을 하려면 팀장이 레포지토리 - settings - branches 들어가서 Lock Branch 옵션 다시 비활성화 하고 작업해야 되는거 같습니다.
   - 그 외 팀 특성에 맞게 옵션들 체크하기



### 2. 팀원 작업 (파일 수정 및 업로드)

1. **프로젝트 레포 클론하기 (팀원)**
   - 이미 클론 되어있으면 `git pull` 사용하기
2. **feature 브랜치 사용하는 경우만 해당 (팀원)**
   - feature : 프로젝트에서 작업을 소분해놓은거 (레포 홈페이지의 projects 탭에서 사용가능) 

   - 해당 작업할 feature 접속
     - ` convert to issue → feature B 페이지 접속 → create a branch 클릭`**(Branch Source는 develop으로 설정)**
     - 로컬 작업 공간의 터미널에`git fetch origin`, `git switch [feature명]` 입력
3. **코드 작업 후 add, commit, push (팀원)**
   - `git clone` 으로  레포지토리를 복제하면, 모든 원격 브랜치의 데이터는 로컬로 다운로드되지만, 실제로 로컬 브랜치로 생성되는 것은 기본 브랜치(대부분 `main` 또는 `master`) 하나뿐임. 
   - 원격 브랜치를 로컬 환경에서 작업하려면 `git branch -r`명령어를 통해 브랜치명을 확인하고,
     `git switch [브랜치명]`을 통해 스위칭 한 후에 작업하면 됨
4. **풀 리퀘스트(PR) 요청 (팀원)**: 작업 branch에서 다른 branch로 파일을 보내도 되는지 타 팀원들에게 허가 요청하는거
   - 해당 branch 페이지 접속 → 상단 Pull requests 클릭 후 PR 작성
   - PR작성 : base branch(= to branch), compare branch(= from branch) 작성 + commit 작성
5. **코드 리뷰(PR 검토) (팀장 및 타 팀원들)**

   - 해당 PR 요청 페이지로 접속하기
   - 반려 : 리뷰 작성 후 save a Review 클릭 → Finish your review 클릭 → Request changes 클릭
   - 수락 : Finish your review  클릭 → approve 클릭 
6. **반려 시 3,4,5작업 반복(팀원)**
7. **승인 시 코드 merge하기 (작업한 팀원 본인이 하는거임)**
- 업로드한 branch 페이지 들어가서 Merge pull request 클릭하면 요청한 branch로 merge 됨
8. **중요 : conflict 발생 시 해결방법**
   - conflict 
     - 내가 로컬에서 작업 중임
     - 타 팀원이 작업한 내용을 [to 브랜치]에 merge 함
     - 내 작업이 끝나서 [to 브랜치]로 pull request 하려고 하면
     - [to branch]에서 버전이 꼬여서 conflict 발생함
   - **해결법 (작업한 팀원 본인이 하는거임)**
     - 로컬 환경에서 `swtich [to 브랜치] → git pull origin [to branch명]`로 최신 코드 가져오기
     - 로컬 환경에서 [from 브랜치]와 [to 브랜치]를 합친후 레포의 [to 브랜치]로 업로드
       - 본인이 `switch [from 브랜치] → git merge [to 브랜치명]` 명령어 입력
       - 충돌나는 부분 팀원과 논의 해서 코드 결정
       - 코드가 잘 돌아가는지 한 번 확인해보기
       - 다시 `add, commit, push [from 브랜치]`
       - 4, 5번 작업 수행 반복

### 3. 부가 기능

1. **프로젝트 보드 및 feature 만들기 (팀장)**

   - 그냥 회의실에 있는 화이트보드 같은 기능

   - 메인페이지 상단 탭 projects → Link a project → Create new project 클릭

   - 해당 탭에서 feature 작성 가능