# demo_for_test

deepevalを使用したLLM評価メトリック集です。翻訳と要約の品質を日本語・英語の両方で評価できます。

## 構成

```
metrics/
├── translation/
│   ├── test_translation_en.py   # 翻訳メトリック（英語）
│   └── test_translation_ja.py   # 翻訳メトリック（日本語）
└── summarization/
    ├── test_summarization_en.py  # 要約メトリック（英語）
    └── test_summarization_ja.py  # 要約メトリック（日本語）
```

## メトリック一覧

### 翻訳 (Translation)

| メトリック名 | 英語名 | 説明 |
|---|---|---|
| 翻訳精度 | Translation Accuracy | 原文の意味を正確に翻訳しているか |
| 翻訳流暢性 | Translation Fluency | ターゲット言語で自然に読めるか |
| 翻訳一貫性 | Translation Consistency | 用語やスタイルが一貫しているか |

### 要約 (Summarization)

| メトリック名 | 英語名 | 説明 |
|---|---|---|
| 要約メトリック（組込） | SummarizationMetric | deepeval組込の要約評価 |
| 要約の簡潔性 | Summarization Conciseness | 簡潔で要点を押さえているか |
| 要約の忠実性 | Summarization Faithfulness | 原文に忠実か（捏造がないか） |
| 要約の網羅性 | Summarization Coverage | 重要なポイントを網羅しているか |
| 要約の一貫性 | Summarization Coherence | 論理的で一貫性があるか |

## セットアップ

```bash
pip install -r requirements.txt
```

### Azure OpenAI の設定

本プロジェクトは社内Azure OpenAIを使用します。以下の手順で設定してください。

1. `.env.example` をコピーして `.env` ファイルを作成します：

```bash
cp .env.example .env
```

2. `.env` ファイルに社内Azure OpenAIの接続情報を入力します：

```
AZURE_API_KEY=your-azure-openai-api-key
AZURE_API_BASE=https://your-resource-name.openai.azure.com/
AZURE_API_VERSION=2024-02-15-preview
AZURE_DEPLOYMENT_NAME=your-deployment-name
```

> **⚠️ 重要**: `.env` ファイルはGitで管理されません（`.gitignore` に登録済み）。API KeyやEndpointをソースコードにハードコードしないでください。

## 実行方法

```bash
# deepeval CLIで全テスト実行
deepeval test run metrics/

# 翻訳メトリックのみ
deepeval test run metrics/translation/

# 要約メトリックのみ
deepeval test run metrics/summarization/
```

> **注意**: 実行前に `.env` ファイルにAzure OpenAIの接続情報が設定されていることを確認してください。
