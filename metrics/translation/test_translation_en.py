"""
Translation evaluation metrics (English) using deepeval.

This module defines test cases and metrics for evaluating
LLM translation quality in English.
"""

from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


# ---------------------------------------------------------------------------
# Metric definitions
# ---------------------------------------------------------------------------

translation_accuracy = GEval(
    name="Translation Accuracy",
    criteria=(
        "Evaluate how accurately the actual output translates the meaning "
        "of the input text. The translation should preserve the original "
        "meaning without adding, omitting, or distorting information."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
)

translation_fluency = GEval(
    name="Translation Fluency",
    criteria=(
        "Evaluate how natural and fluent the translated text reads in the "
        "target language. The output should use proper grammar, natural word "
        "order, and idiomatic expressions appropriate for the target language."
    ),
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

translation_consistency = GEval(
    name="Translation Consistency",
    criteria=(
        "Evaluate whether terminology and style are used consistently "
        "throughout the translation. Key terms should be translated the same "
        "way each time they appear."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)


# ---------------------------------------------------------------------------
# Sample test cases: Japanese → English
# ---------------------------------------------------------------------------

test_cases_ja_to_en = [
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
# Sample test cases: English → Japanese
# ---------------------------------------------------------------------------

test_cases_en_to_ja = [
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
# Evaluation helpers
# ---------------------------------------------------------------------------

ALL_METRICS = [translation_accuracy, translation_fluency, translation_consistency]


def evaluate_translation_en(test_case: LLMTestCase) -> None:
    """Run all English translation metrics against a single test case."""
    for metric in ALL_METRICS:
        assert_test(test_case, [metric])
