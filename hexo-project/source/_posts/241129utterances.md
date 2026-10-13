---
title: "[블로그]헥소테마에서 댓글기능 facebook에서 utterances로 변경하기"
date: 2024-11-28 23:23:25
tags:
  - "Hexo"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">헥소(Hexo) 블로그의 기존 페이스북 댓글 기능을 깃허브(GitHub) 아이디로 로그인하여 사용할 수 있는 utterances로 교체하는 방법을 정리한 글이다.
    comment.jsx에 utterances 스크립트를 추가하고, _config.yml에서 페이스북 앱 ID만 제거하는 방식으로 댓글 시스템을 간단히 전환할 수 있다.</p>
</div>

<!-- more -->

헥소블로그에서 기존 제공하는 페이스북 댓글기능을 사용하고 있었는데 더이상 페이스북을 사용하지않아 삭제하고 싶었다.  
그러다 우연히 전회사 팀장님 개발블로그에 깃헙아이디로 로그인하여 쓸 수 있는 댓글기능을 보고 유레카를 외쳤다.

팀장님께 여쭤보니 손수 보기편한 링크를 주셔서 쉽게 적용가능했다. (감사합니다 팀장님!)

# 참고한 블로그

  * [아웃스탠딩보이님의 블로그에 댓글 기능 추가하기 (ft. Utterances)](https://velog.io/@outstandingboy/Github-%EB%B8%94%EB%A1%9C%EA%B7%B8%EC%97%90-%EB%8C%93%EA%B8%80-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0-ft.-Utterances)
  * [BAEKDEV님의 utterances를 블로그 댓글로 적용하기](https://baek.dev/post/4/)

위 두 포스팅에서 친절하게 잘 설명되어있어 금방 적용가능하다.  
다른 점이 있다면 헥소블로그테마는 리액트 jsx기반이다.

  
  
  

# 댓글넣기

comment.jsx 파일에서 utterances를 추가해줘야한다

  * 파일위치: layout/common/cpmment.jsx

아래는 기존 코드를 주석처리하고 utteranc코드를 추가한 모습이다.

```jsx
module.exports = class extends Component {
    render() {
        const { config, page, helper } = this.props;
        const { __ } = helper;
        const { comment } = config;
        if (!comment || typeof comment.type !== 'string') {
            return null;
        }

        return <div class="card">
            <div class="card-content">
                {/*
				<h3 class="title is-5">{__('article.comments')}</h3> 
				{(() => {
                    try {
                        let Comment = view.require('comment/' + comment.type);
                        Comment = Comment.Cacheable ? Comment.Cacheable : Comment;
                        return <Comment config={config} page={page} helper={helper} comment={comment} />;
                    } catch (e) {
                        logger.w(`Icarus cannot load comment "${comment.type}"`);
                        return null;
                    }
                })()}
				*/}
				<script src="https://utteranc.es/client.js"
						repo="리포지토리 이름"
						issue-term="pathname"
						theme="github-light"
						crossorigin="anonymous"
						async>
				</script>
            </div>
        </div>;
    }
};
```

  
  
  

# 페이스북 연결해제하기

  * 파일위치: theme/hexo-theme-icarus/_config.yml

위 파일에서 

  1. `fb_app_id`를 검색하여 지워준다.
  2. `comment:`를 검색하여 facebook을 지우면 안된다. 지우게되면 comment자체가 비활성화된다.

#[Hexo](/tags/Hexo/)
