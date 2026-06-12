"""
翻訳評価メトリック（日本語）- deepevalを使用

このモジュールでは、LLMの翻訳品質を評価するための
テストケースとメトリックを日本語で定義しています。
"""

from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


# ---------------------------------------------------------------------------
# メトリック定義
# ---------------------------------------------------------------------------

翻訳精度 = GEval(
    name="翻訳精度",
    criteria=(
        "実際の出力が入力テキストの意味をどれだけ正確に翻訳しているかを評価してください。"
        "翻訳は、情報の追加、省略、歪曲なしに、元の意味を保持する必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
)

翻訳流暢性 = GEval(
    name="翻訳流暢性",
    criteria=(
        "翻訳されたテキストがターゲット言語でどれだけ自然で流暢に読めるかを評価してください。"
        "出力は、適切な文法、自然な語順、ターゲット言語に適した慣用表現を使用する必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

翻訳一貫性 = GEval(
    name="翻訳一貫性",
    criteria=(
        "翻訳全体を通じて、用語とスタイルが一貫して使用されているかを評価してください。"
        "重要な用語は、出現するたびに同じ方法で翻訳される必要があります。"
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)


# ---------------------------------------------------------------------------
# サンプルテストケース：日本語 → 英語
# ---------------------------------------------------------------------------

テストケース_日英 = [
    LLMTestCase(
        input="日本の四季は美しく、特に春の桜と秋の紅葉は多くの観光客を魅了しています。",
        actual_output=(
            "Japan's four seasons are beautiful, and the cherry blossoms in "
            "spring and autumn foliage in particular attract many tourists."
        ),
        expected_output=(
            "The four seasons in Japan are beautiful, especially the cherry "
            "blossoms in spring and the autumn leaves captivate many tourists."
        ),
    ),
    LLMTestCase(
        input="人工知能の発展により、多くの産業で自動化が進んでいます。",
        actual_output=(
            "With the development of artificial intelligence, automation "
            "is advancing in many industries."
        ),
        expected_output=(
            "Due to advances in artificial intelligence, automation is "
            "progressing across many industries."
        ),
    ),
    LLMTestCase(
        input="持続可能な開発目標（SDGs）は、2030年までに達成すべき17の目標を掲げています。",
        actual_output=(
            "The Sustainable Development Goals (SDGs) set forth 17 goals "
            "to be achieved by 2030."
        ),
        expected_output=(
            "The Sustainable Development Goals (SDGs) outline 17 goals "
            "that should be achieved by 2030."
        ),
    ),
]


# ---------------------------------------------------------------------------
# サンプルテストケース：英語 → 日本語
# ---------------------------------------------------------------------------

テストケース_英日 = [
    LLMTestCase(
        input=(
            "Climate change is one of the most pressing challenges facing "
            "humanity today."
        ),
        actual_output="気候変動は、今日の人類が直面している最も差し迫った課題の一つです。",
        expected_output="気候変動は、現在人類が直面している最も緊急な課題の一つです。",
    ),
    LLMTestCase(
        input=(
            "The rapid growth of e-commerce has transformed the retail "
            "industry worldwide."
        ),
        actual_output="電子商取引の急速な成長は、世界中の小売業界を変革しました。",
        expected_output="Eコマースの急速な成長により、世界中の小売業が変革されました。",
    ),
    LLMTestCase(
        input=(
            "Effective communication is essential for successful teamwork "
            "in any organization."
        ),
        actual_output=(
            "効果的なコミュニケーションは、あらゆる組織における "
            "チームワークの成功に不可欠です。"
        ),
        expected_output=(
            "効果的なコミュニケーションは、どのような組織においても "
            "チームワークを成功させるために不可欠です。"
        ),
    ),
]


# ---------------------------------------------------------------------------
# 評価ヘルパー
# ---------------------------------------------------------------------------

全メトリック = [翻訳精度, 翻訳流暢性, 翻訳一貫性]


def 翻訳評価_日本語(test_case: LLMTestCase) -> None:
    """単一のテストケースに対してすべての日本語翻訳メトリックを実行します。"""
    for metric in 全メトリック:
        assert_test(test_case, [metric])
