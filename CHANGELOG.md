# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [3.1.0](https://github.com/ReRokutosei/yahei-sarasa/compare/v3.0.0...v3.1.0) (2025-07-10)


### Features

* **msyh:** 增加配置项`MSYH_ENABLE_EXTRA_ITALIC`，可选是否生成额外的斜体字重 ([ea20df1](https://github.com/ReRokutosei/yahei-sarasa/commit/ea20df1571213d079c5c6091a6eec9d86fa11b19))
* **workflow:** 增加简单的进度条输出 ([099efc8](https://github.com/ReRokutosei/yahei-sarasa/commit/099efc8ebb0a06870361f9f1fbbcb3b0fdf3dc0c))


### Bug Fixes

* **msyh:** 修复字体映射顺序错乱问题 ([360cfe7](https://github.com/ReRokutosei/yahei-sarasa/commit/360cfe764de9b5dbac6b9a14e3866d6c77b9cfee))
* **msyh:** 移除了`failed_count`计数器，在发现任何字体缺失时终止流程 ([fcc9b76](https://github.com/ReRokutosei/yahei-sarasa/commit/fcc9b76e643be455f415ff196ad4af0de2be92da))

## [3.0.0](https://github.com/ReRokutosei/yahei-sarasa/compare/v2.2.0...v3.0.0) (2025-07-06)


### ⚠ BREAKING CHANGES

* **utils:** 移除project_utils.py

### Features

* **msyh:** 新增可选将单独的TTF文件复制到结果子目录 ([edf5179](https://github.com/ReRokutosei/yahei-sarasa/commit/edf5179805db7ecbebc04f8dad884b9f9e972dba))
* **parallel:** 实现OTF转TTF并行处理优化 ([ef6a4a1](https://github.com/ReRokutosei/yahei-sarasa/commit/ef6a4a152629ba20ddb9280aef4543dab4b0d7bf))


* **utils:** 重构工具函数结构，优化代码组织 ([225aadf](https://github.com/ReRokutosei/yahei-sarasa/commit/225aadf474eb1663a93cda660f68d2c83a3ce657))

## [2.2.0](https://github.com/ReRokutosei/yahei-sarasa/compare/v2.1.0...v2.2.0) (2025-07-05)


### Features

* **otf2ttf:** 支持传入otf文件 ([b8863ce](https://github.com/ReRokutosei/yahei-sarasa/commit/b8863ce86374b758c45e343f7f4800070c7b0b72))
* **project_util:** custom模式支持传入多个字体包 ([fd3f597](https://github.com/ReRokutosei/yahei-sarasa/commit/fd3f5970fc632f47ae8704abdb61b5b8d3ca99eb))

## [2.1.0](https://github.com/ReRokutosei/yahei-sarasa/compare/v2.0.0...v2.1.0) (2025-07-04)


### Features

* **auto_all:** 增加输出版本报告 ([8db5ae3](https://github.com/ReRokutosei/yahei-sarasa/commit/8db5ae389fd6f99e689944435ea3cb0c332d8892))
* **config,msyh,segoe,auto:** 支持微软雅黑数字(等距/不等距)与Segoe UI间距(宽松/紧凑)调整 ([c285b5c](https://github.com/ReRokutosei/yahei-sarasa/commit/c285b5cb7036916694f2d8f95e50c1e747be617d))
* **custom_mode:** 添加custom模式，可以自定义传入的字体源文件 ([5993790](https://github.com/ReRokutosei/yahei-sarasa/commit/5993790e7613ddf484fcec0ddd6d6c9cd119a3ed))
* **fetch_inter:** 为Inter添加在线版本信息对照 ([842cdd5](https://github.com/ReRokutosei/yahei-sarasa/commit/842cdd5aa3f1a4602d84ae6ea6beb85ca93263f4))
* **fetch:** 为两个fetch文件添加了下载进度输出，并为fetch_sarasa增加哈希校验 ([72a2056](https://github.com/ReRokutosei/yahei-sarasa/commit/72a20568c98facbe1ad2b7829dfc472e57b06ec6))


### Bug Fixes

* **all:** 修复 online 模式下源字体包获取失败、生成文件无法复制到子文件夹及日志错位问题 ([939551c](https://github.com/ReRokutosei/yahei-sarasa/commit/939551c808ff3b3e8fcbedc3068343577f472461))
* **fetch_inter:** 修复缺失的DOWNLOAD_TIMEOUT 键值 ([5c6c1fe](https://github.com/ReRokutosei/yahei-sarasa/commit/5c6c1fee56c3ffd042a4b5e5f9e465d9160d62cf))
* **fetch_sarasa:** 修复重复输出日志的问题 ([b3ceee3](https://github.com/ReRokutosei/yahei-sarasa/commit/b3ceee34454882abdc632e8d4dfc379ec124c53d))
* **version_report:** 修复报告文本写入顺序错误的问题 ([2318343](https://github.com/ReRokutosei/yahei-sarasa/commit/2318343fe0808b6a7a170439e37e891b7ed754e3))

# [2.0.0](https://github.com/ReRokutosei/ZH-Font-Replacement/compare/v1.2.0...v2.0.0) (2025-07-01)



# [1.2.0](https://github.com/ReRokutosei/ZH-Font-Replacement/compare/v1.1.0...v1.2.0) (2025-06-29)


* refactor(core)!: 精简重构字体生成与主流程 ([13efa5a](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/13efa5a3551355768b7bf9fac13f875f930c6f59))


### Bug Fixes

* **auto_all:** HansCode 编程字体输出到正确的结果子目录 ([bdaaec3](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/bdaaec37369b5a5131dd0f26a392a181c2325c9e))
* **config:** 修复 OTHER_COPY 配置项为 None 时异常，FFPYTHON_PATH 强制从 yaml 读取 ([1d3b060](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/1d3b06094e6a7064237db870d207f3b978b0f29e))
* **copy_result:** 自动复制 HansCode-*.ttf 编程字体到结果目录 ([75837ba](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/75837bab9fbab26f023af04f1f6616bad938793f))


### Features

* **automation:** 自动化拆分与主流程重构，修正字重与压缩包处理 ([32c7de4](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/32c7de403b11510813f339ef5cd015ca2fb691ef))
* **config,build,docs:** 支持更多字重、可选流程与本地源兜底，提升自动化与文档指引 ([7a7081a](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/7a7081aa07eb6ba01837f14274e949f4d1faed6b))
* **version:** 生成的所有字体Version字段自动添加当前日期 ([0867d88](https://github.com/ReRokutosei/ZH-Font-Replacement/commit/0867d8817e2aaf8b7e843c36df406892fa4496e6))


### BREAKING CHANGES

* - 改为依赖 config.yaml 配置
- 目录结构和部分行为更为自动化，
* **automation:** - Windows 用户需手动指定 FFPYTHON_PATH，且只需在主控环境 pip 安装依赖
* **config,build,docs:** - 需根据新配置文件格式调整 auto_configs.py
- 需在 source_files 目录手动放置字体包以支持本地兜底
- 依赖包和本地源文件准备方式有重大简化，用户无需再下载体积巨大的 Sarasa-TTF-*.7z



# [1.1.0](https://github.com/ReRokutosei/ZH-Font-Replacement/compare/v1.0.0...v1.1.0) (2025-03-28)



# 1.0.0 (2023-05-09)
