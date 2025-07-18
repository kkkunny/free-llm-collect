# free-llm-collect
搜集免费的LLM（大语言模型）

> 之前一直用的公司的GPT API key做机器人，结果后来被收回了，又不想掏钱，只能上网寻觅下免费的LLM API，这里做个记录
> 
> 注：这里记录的都是可以用来部署的项目或者官方API

+ 综合
  + [OpenRouter](https://openrouter.ai/deepseek/deepseek-r1:free)
    + 使用体验：响应较快
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：视模型而异
    + 是否需要外网环境部署：未知
  + [Poixe AI](https://poixe.com/)
    + 使用体验：响应较快
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：未知
+ DeepSeek
  + [硅基流动提供的免费蒸馏R1](https://cloud.siliconflow.cn/models)
    + 使用体验：响应很慢
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：是
    + 是否需要外网环境部署：否
  + [无问芯穹提供的免费R1](https://cloud.infini-ai.com/promotion)
    + 使用体验：响应较快
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
+ GPT
  + [官网无需登录ChatGPT逆向](https://github.com/missuo/FreeGPT35)
    + 使用体验：响应慢，偶尔抽风，不稳定
    + 是否需要登录或cookie：无需
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
  + [字节Coze海外平台提供的免费GPT](https://github.com/deanxv/coze-discord-proxy)
    + 使用体验：响应慢，有次数限制，十分稳定
    + 是否需要登录或cookie：因为使用了discord，需要传discord的cookie，cookie生命周期很长
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
  + [DuckDuckGo提供的免费GPT3.5](https://github.com/missuo/FreeDuckDuckGo)
    + 使用体验：响应较快，较稳定
    + 是否需要登录或cookie：无需
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
  + [ChandlerAi提供的免费GPT3.5](https://github.com/kkkunny/ChandlerAiAPI)
    + 使用体验：响应较快，较稳定
    + 是否需要登录或cookie：需要自己抓取token
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
+ Claude
  + [DuckDuckGo提供的免费Claude3Haiku](https://github.com/missuo/FreeDuckDuckGo)
    + 使用体验：响应较快，较稳定
    + 是否需要登录或cookie：无需
    + 其他：这个项目没有增加Claude模型，可以自行寻找其他项目，或者自己改
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
+ Bing Copilot
  + [BingAI逆向](https://github.com/Harry-zklcdc/go-proxy-bingai)
    + 使用体验：响应很慢，不稳定
    + 是否需要登录或cookie：需要在UI界面中登录或填cookie
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
+ Gemini
  + [Gemini免费套餐](https://ai.google.dev/models/gemini?hl=zh-cn)
    + 使用体验：响应很快，十分稳定，免费版有调用量限制，对于个人而言完全够用了
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：是
    + 是否需要外网环境访问：是
+ LLama
  + ~~[nvidia免费套餐](https://build.nvidia.com)~~
    + ~~使用体验：响应很快，十分稳定，尚不清楚调用量上限~~
    + ~~是否需要登录或cookie：使用nvidia提供的API key~~
    + ~~是否需要外网环境访问：否~~
    + 有免费额度，用完即没
  + [HuggingFace提供的免费Chat逆向](https://github.com/kkkunny/HuggingChatAPI)
    + 这里有个我自己写的，已有的一个python的项目我没调用成功
    + 使用体验：响应较快，较稳定，尚不清楚调用量上限
    + 是否需要登录或cookie：需要cookie
    + 是否能够函数调用：否
    + 是否需要外网环境部署：是
  + [CloudFlare免费套餐](https://playground.ai.cloudflare.com)
    + 使用体验：响应很快，十分稳定，尚不清楚调用量上限
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境访问：否
  + [Groq免费套餐](https://groq.com)
    + 使用体验：响应较快，不稳定，有封号风险，挂的日本的梯子也没聊啥就被封了
    + 是否需要登录或cookie：需要API key
    + 是否需要外网环境访问：是
  + [ChandlerAi提供的免费LLama3](https://github.com/kkkunny/ChandlerAiAPI)
    + 使用体验：响应较快，较稳定
    + 是否需要登录或cookie：需要抓token
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
+ 国产模型
  + [智谱清言免费套餐](https://open.bigmodel.cn/console/overview)
    + 使用体验：响应较快，很稳定，仅限glm-4-flash免费
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：是
    + 是否需要外网环境部署：否
  + [阿里 通义千问逆向](https://github.com/LLM-Red-Team/qwen-free-api)
    + 使用体验：响应较快，很稳定
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [月之暗面 Kimi逆向](https://github.com/LLM-Red-Team/kimi-free-api)
    + 使用体验：响应较快，很稳定，据说有封号风险
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [阶跃星辰 跃问逆向](https://github.com/LLM-Red-Team/step-free-api)
    + 使用体验：响应较快，很稳定
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [智谱清言 GLM逆向](https://github.com/LLM-Red-Team/glm-free-api)
    + 使用体验：响应较快，很稳定
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [讯飞 星火逆向](https://github.com/LLM-Red-Team/spark-free-api)
    + 使用体验：响应较快，很稳定
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [秘塔AI逆向](https://github.com/LLM-Red-Team/metaso-free-api)
    + 使用体验：未使用过
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [海螺AI逆向](https://github.com/LLM-Red-Team/hailuo-free-api)
    + 使用体验：未使用过
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
  + [聆心智能逆向](https://github.com/LLM-Red-Team/emohaa-free-api)
    + 使用体验：未使用过
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否
+ 其他模型
  + [siliconflow](https://siliconflow.cn/zh-cn/)
    + 使用体验：响应较快，但免费的都是一些国内的非旗舰模型，另有FLUX.1、sd等文生图模型**限时免费！**
    + 是否需要外网环境部署：否
  + [mistral免费套餐](https://console.mistral.ai/)
    + 使用体验：响应较快，不太稳定
    + 是否需要登录或cookie：需要API key
    + 是否需要外网环境部署：否
    + 是否能够函数调用：是
  + [glhf免费API](https://glhf.chat/landing/home)
    + 使用体验：响应较慢。包含一些开源的旗舰模型，还可以自己部署模型
    + 是否需要登录或cookie：需要API key
    + 是否能够函数调用：否
    + 是否需要外网环境部署：否