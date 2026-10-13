---
title: "[특강후기]JS로 디스코드 봇만들기"
date: 2021-03-25 16:51:28
tags:
  - "Discord"
  - "Websocket"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'JS로 디스코드 봇만들기'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    실무 적용 사례를 통해 개발자의 역할과 협업, 지속적인 학습의 중요성을 확인할 수 있다.</p>
</div>

<!-- more -->

좋은 기회로 디스코드 챗봇을 만드는 온라인 특강을 듣게되었다.  
정말 재미있었다!

# 순서

## vs code에 npm 설치하기

  1. `npm install`: npm을 설치한다.
  2. `npm run dev`: 설치한 npm을 실행한다.

  
  
  

## [디스코드 디벨로퍼](https://discord.com/developers/applications)에서 챗봇등록하기

  1. `new appication` 클릭
  2. `add bot` 클릭 후 `yes do it` 후 토큰을 복사

![](/img/210226discordbot1.png)  
![](/img/210226discordbot2.png)  
토큰을 통해서 채팅을 CR할 수 있기때문에 실제 서버에 배포한다면 토큰은 절대 공개되서는 안된다.

  3. vs code의 터미널에서 config.json에 복사한 토큰을 붙여넣는다.

![](/img/210226discordbot3.png)

  4. [디스코드 디벨로퍼 포털](https://discord.com/developers/applications)에서 생성한 채널을 클릭한 뒤 General Information에서 CLIENT ID 토큰 복사

![](/img/210226discordbot4.png)

  5. [디스코드 permissions calculator](https://finitereality.github.io/permissions-calculator/?v=8)에서 권한주기

     * add 클릭 → 승인  
![](/img/210226discordbot5.png)
  6. [디스코드](https://discord.com/channels/@me)에서 채널이 생성된 것을 확인하기

  
  

## vs code에서 코딩하기

`!투표`를 이용해서 제목과 투표지를 띄어쓰기로 입력하면 해당 입력값으로 투표하기를 생성해주는 챗봇을 만들어보자.

```js
export default async function vote(message, args) {
  const voteEmojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"];

  const question = args.shift();

  if (args.length < 1 || args.length > 5) {
    message.reply("One to five options are required. 선택 항목은 1-5개만 지원합니다.");
  }

  const embed = new MessageEmbed();

  let description = "";
  args.forEach((arg, i) => {
    description += `${voteEmojis[i]}: ${arg}\n`;
  });

  embed.setTitle("🗳 " + question);
  embed.setDescription(description);

  const vote = await message.reply("Vote", { embed: embed });
  args.forEach(async (arg, i) => {
    await vote.react(voteEmojis[i]);
  });
}
```

![완성된 모습](/img/210226discordbot6.png)

  * [전체 소스코드](https://github.com/sowon-dev/simple-discord-chatbot-js)

  
  
  

# 웹소캣 vs HTTP

HTTP의 경우 클라이언트의 요청이 없으면 서버는 먼저 말을 걸 수 없다.  
웹소켓은 서버가 클라이언트에게 먼저 말(메세지)을 걸수있다.

  
  
  

# 서버 확인하는 사이트

서버가 정상적인지 확인하는 사이트 : <https://isitup.org/>

#[Discord](/tags/Discord/)[Websocket](/tags/Websocket/)
