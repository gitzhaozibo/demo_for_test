"""
要約評価メトリック（日本語）- deepevalを使用

このモジュールでは、LLMの要約品質を評価するための
テストケースとメトリックを日本語で定義しています。
"""

from deepeval import assert_test
from deepeval.metrics import GEval, SummarizationMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


# ---------------------------------------------------------------------------
# メトリック定義
# ---------------------------------------------------------------------------

要約メトリック_組込 = SummarizationMetric(
    threshold=0.7,
    assessment_questions=[
        "要約は元のテキストの主要なポイントを捉えていますか？",
        "要約は原文に対して事実の誤りがありませんか？",
        "要約は不要な詳細を含んでいませんか？",
    ],
)

要約_簡潔性 = GEval(
    name="要約の簡潔性",
    criteria=(
        "要約が簡潔で要点を押さえているかを評価してください。"
        "要約は、不要な詳細、繰り返し、冗長な表現なしに、"
        "本質的な情報を捉える必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

要約_忠実性 = GEval(
    name="要約の忠実性",
    criteria=(
        "要約が元のテキストに忠実であるかを評価してください。"
        "要約には、原文に存在しない、または原文から推論できない情報が"
        "含まれていてはなりません。捏造された事実が導入されていないことを確認してください。"
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

要約_網羅性 = GEval(
    name="要約の網羅性",
    criteria=(
        "要約が元のテキストのすべての重要なポイントをカバーしているかを評価してください。"
        "原文の重要な事実、論点、結論が要約に反映されている必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
)

要約_一貫性 = GEval(
    name="要約の一貫性",
    criteria=(
        "要約が整理されており、一貫性があるかを評価してください。"
        "要約は論理的に流れ、文が意味のある形でつながり、"
        "単独でも理解しやすいものである必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)


# ---------------------------------------------------------------------------
# サンプルテストケース：英語テキストの要約
# ---------------------------------------------------------------------------

テストケース_英語要約 = [
    LLMTestCase(
        input=(
            "Artificial intelligence (AI) has made significant strides in "
            "recent years, particularly in the fields of natural language "
            "processing, computer vision, and robotics. Companies across "
            "various industries are adopting AI to automate processes, "
            "improve decision-making, and enhance customer experiences. "
            "However, the rapid advancement of AI also raises concerns "
            "about job displacement, privacy, and ethical implications. "
            "Governments and organizations worldwide are working to "
            "establish regulations and guidelines to ensure responsible "
            "AI development and deployment."
        ),
        actual_output=(
            "AIは自然言語処理、コンピュータビジョン、ロボティクスの分野で大きく進歩し、"
            "多くの産業で導入が進んでいます。しかし、雇用喪失やプライバシー、倫理的問題への"
            "懸念もあり、世界中で規制の整備が進められています。"
        ),
        expected_output=(
            "AI技術はNLP、コンピュータビジョン、ロボティクスで飛躍的に進歩し、"
            "産業界での活用が広がっています。一方、雇用やプライバシー、倫理面の課題があり、"
            "各国が規制整備に取り組んでいます。"
        ),
    ),
    LLMTestCase(
        input=(
            "Remote work has become increasingly popular since the COVID-19 "
            "pandemic. Many companies have adopted hybrid work models that "
            "allow employees to split their time between home and the office. "
            "Studies show that remote work can increase productivity and "
            "job satisfaction, but it also presents challenges such as "
            "isolation, difficulty in collaboration, and blurred boundaries "
            "between work and personal life. Organizations are investing in "
            "digital tools and policies to address these challenges."
        ),
        actual_output=(
            "コロナ禍以降、リモートワークが普及し、多くの企業がハイブリッド型勤務を導入しました。"
            "生産性向上や満足度の向上がある一方、孤立感やワークライフバランスの課題もあり、"
            "企業はデジタルツールや制度の整備に投資しています。"
        ),
        expected_output=(
            "パンデミック以降、リモート・ハイブリッドワークが拡大しました。"
            "生産性や満足度が向上する反面、孤立やワークライフバランスの課題があり、"
            "企業は対策に投資しています。"
        ),
    ),
]


# ---------------------------------------------------------------------------
# サンプルテストケース：日本語テキストの要約
# ---------------------------------------------------------------------------

テストケース_日本語要約 = [
    LLMTestCase(
        input=(
            "日本の少子高齢化は深刻な社会問題となっています。出生率の低下と平均寿命の"
            "延びにより、労働人口が減少し、社会保障制度への負担が増大しています。"
            "政府は子育て支援策の拡充や外国人労働者の受け入れ拡大などの対策を講じて"
            "いますが、根本的な解決には至っていません。"
        ),
        actual_output=(
            "日本では少子高齢化により労働力不足と社会保障の負担増が進んでいます。"
            "政府は子育て支援や外国人労働者受け入れなどの施策を実施していますが、"
            "根本的な解決策はまだ見つかっていません。"
        ),
        expected_output=(
            "少子高齢化による労働人口減少と社会保障負担の増大が日本の深刻な課題です。"
            "政府の対策にもかかわらず、抜本的な解決には至っていません。"
        ),
    ),
    LLMTestCase(
        input=(
            "近年、日本ではキャッシュレス決済の普及が加速しています。QRコード決済や"
            "電子マネー、クレジットカードの利用が増え、政府もキャッシュレス化を推進して"
            "います。しかし、高齢者のデジタルリテラシーの問題や、小規模店舗の導入コスト、"
            "セキュリティへの懸念など、課題も残っています。2025年までに"
            "キャッシュレス決済比率を40%にする目標が掲げられています。"
        ),
        actual_output=(
            "日本でキャッシュレス決済が急速に普及しており、政府は2025年までに"
            "決済比率40%を目指しています。一方、高齢者のデジタル対応や小規模店舗の"
            "コスト、セキュリティなどの課題もあります。"
        ),
        expected_output=(
            "日本ではキャッシュレス決済の普及が進み、政府は40%の目標を設定しています。"
            "高齢者対応、導入コスト、セキュリティ面での課題が残っています。"
        ),
    ),
]


# ---------------------------------------------------------------------------
# 評価ヘルパー
# ---------------------------------------------------------------------------

全GEvalメトリック = [要約_簡潔性, 要約_忠実性, 要約_網羅性, 要約_一貫性]

全メトリック = [要約メトリック_組込] + 全GEvalメトリック


def 要約評価_日本語(test_case: LLMTestCase) -> None:
    """単一のテストケースに対してすべての日本語要約メトリックを実行します。"""
    for metric in 全メトリック:
        assert_test(test_case, [metric])
