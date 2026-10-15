# 《双姝商途》V23.36R1 外部AI读取失败排障（非剧本正文）

> 状态：仓库 **PUBLIC**，默认 `main` 是旧版。最新待审为 `review/shuangshu-v23.36r1-candidate-20261016`；正式CURRENT仍V23.33R1。PGS30=HOLD。此文仅解决读取通道问题，不表示任何外部AI已经读完64集。

## 已实核事实

- GitHub连接按明确branch + path读取：完整正文 **64集、268场**，源文本 **75,133个JS字符，1,906行**；blob `edeb513edcfe9552c13e56bd1c9c5ed7fbf50734`。
- 同分支的 `reviews/sourcepack_v23.36/episodes/E024.md`、`BATCH_INDEX.md`、`canon/PROJECT_CANON.md` 均实际存在，可以通过GitHub连接读取。
- 其它某些AI的网页通道可能对 `github.com`、`raw.githubusercontent.com` 返回 `chrome-error` / 空响应 / `DisabledError`，这**只证明其本次工具没有取到内容**，并不能证明仓库私有、文件失踪或作者传了错误链接。
- 一个AI称branch commit `87781c2`存在，只证明它见过当时的导航提交；**最新版候选文件在此后提交仍可保持同一Git Blob，不能拿历史短哈希直接证明读到了正文**。
- 读取原始长文件也可能在模型工具层被截断。即使列出64个文件名和标题，也不等于看完64集内容。

## 最推荐的读取方法（依次尝试，失败及时停止）

1. **拥有GitHub连接器/MCP/仓库API权限的AI：优先使用连接器按精确branch和path读取。** 不使用默认main。精确参数：`repository_full_name=chen47206017-cpu/AI-Drama-Production-Pipeline`，`ref=review/shuangshu-v23.36r1-candidate-20261016`，`path=projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md`。
2. **允许HTTP的终端/代码环境：直接下载原始Markdown到本地，以文件读取而非浏览器页面抽取方式处理。**（不经过第三方镜像转存）
   ```bash
   curl -fL --retry 2 -o V23.36R1_CANDIDATE_E001-E064.md "https://raw.githubusercontent.com/chen47206017-cpu/AI-Drama-Production-Pipeline/bd4d74bd964fdbb6f4de07c480e394262e4b3b1d/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md"
   ```
   固定commit的raw地址可避免分支中斜杠被部分解析器错误拆分。
3. **GitHub REST API（若模型确实支持调用，避免只靠网页总结）：**
   `https://api.github.com/repos/chen47206017-cpu/AI-Drama-Production-Pipeline/contents/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md?ref=review%2Fshuangshu-v23.36r1-candidate-20261016`
   可能返回JSON Base64或由连接器直接解码的文本；按实际返回格式处理，**不能把Base64或元数据当剧本正文**。也可以用已确认blob：
   `https://api.github.com/repos/chen47206017-cpu/AI-Drama-Production-Pipeline/git/blobs/edeb513edcfe9552c13e56bd1c9c5ed7fbf50734`
4. **如果仅网页浏览可用：** 先试[固定提交的源文件](https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/bd4d74bd964fdbb6f4de07c480e394262e4b3b1d/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md)；若长文本被截断，改用[64集单独文本](reviews/sourcepack_v23.36/EPISODE_INDEX.md)或[8个批次](reviews/sourcepack_v23.36/BATCH_INDEX.md)；每集均核全文，不要靠目录补全。
5. **如果该AI的所有网页请求均报错、无MCP/HTTP/本地文件功能：** 该会话无法直接读取GitHub。用户可在自己的浏览器打开上述固定raw链接，保存为UTF-8的`.md`，再**直接上传文件到该AI的会话**（若该平台支持附件），让AI从上传文件逐批读；上传和解析后仍必须验证来源与阅读覆盖。不建议为了绕过限制将未公开剧本上传到不可信第三方加速镜像。

## 不允许的错误报告

- 错误：`GitHub raw返回空内容 → 仓库没有V23.36原文`。正确：`本AI当前访问通道UNREAD；另用GitHub接口或附件取证`。
- 错误：`能读V23.33 → 可以推测V23.36已修改内容`。正确：`V23.36 UNREAD，禁止以V23.33冒充最新审稿`。
- 错误：`文件夹列出64个名字 → 64集全文100%读完`。正确：`目录核验PASS，正文阅读另查`。
- 错误：`E002台词在E005，E024为车厢第三箱事故，E040–E048返回现代`。正确：须逐场从候选E002/E024/E040–E048获取引证，无法读取就不作确定结论。

## 检查实际下载文件的完整性

如外部AI有Python终端，文件以UTF-8解码后核**Git blob**与结构：

```python
from pathlib import Path
import hashlib, re
p = Path("V23.36R1_CANDIDATE_E001-E064.md")
raw = p.read_bytes()
sha1 = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
text = raw.decode("utf-8")
eps = [int(x) for x in re.findall(r"(?m)^# E(\d{3})《", text)]
scenes = len(re.findall(r"(?m)^### 【", text))
print({"git_blob":sha1,"episodes":len(eps),"scenes":scenes})
assert sha1 == "edeb513edcfe9552c13e56bd1c9c5ed7fbf50734"
assert eps == list(range(1,65)) and scenes == 268
```

**注意：** 即使验证了原文身份、集数与场数，仍未证明AI真正看完并理解每集。必须执行审稿提示词中的每集双引证及跨集时空、道具、账款的事实门禁。

[完整64集](https://github.com/chen47206017-cpu/AI-Drama-Production-Pipeline/blob/bd4d74bd964fdbb6f4de07c480e394262e4b3b1d/projects/shuangshu-shangtu/scripts/candidates/V23.36R1_CANDIDATE_E001-E064.md) · [全新来源锁定审稿提示词](reviews/sourcepack_v23.36/EXTERNAL_AI_VERIFIED_REVIEW_PROMPT.md)
