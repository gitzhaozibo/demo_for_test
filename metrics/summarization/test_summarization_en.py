"""
Summarization evaluation metrics (English) using deepeval.

This module defines test cases and metrics for evaluating
LLM summarization quality in English.
"""

from deepeval import assert_test
from deepeval.metrics import GEval, SummarizationMetric
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


# ---------------------------------------------------------------------------
# Metric definitions
# ---------------------------------------------------------------------------

summarization_builtin = SummarizationMetric(
    threshold=0.7,
    assessment_questions=[
        "Does the summary capture the main points of the original text?",
        "Is the summary free from factual errors relative to the source?",
        "Does the summary avoid including unnecessary details?",
    ],
)

summarization_conciseness = GEval(
    name="Summarization Conciseness",
    criteria=(
        "Evaluate whether the summary is concise and to the point. "
        "The summary should capture the essential information without "
        "unnecessary details, repetition, or verbose expressions."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

summarization_faithfulness = GEval(
    name="Summarization Faithfulness",
    criteria=(
        "Evaluate whether the summary is faithful to the original text. "
        "The summary should not contain any information that is not present "
        "in or cannot be inferred from the source text. No hallucinated "
        "facts should be introduced."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)

summarization_coverage = GEval(
    name="Summarization Coverage",
    criteria=(
        "Evaluate whether the summary covers all the key points of the "
        "original text. Important facts, arguments, and conclusions from "
        "the source should be represented in the summary."
    ),
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
)

summarization_coherence = GEval(
    name="Summarization Coherence",
    criteria=(
        "Evaluate whether the summary is well-organized and coherent. "
        "The summary should flow logically, with sentences connected in a "
        "meaningful way, and should be easy to understand on its own."
    ),
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
    ],
    threshold=0.7,
)


# ---------------------------------------------------------------------------
# Sample test cases: English summarization
# ---------------------------------------------------------------------------

test_cases_en = [
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
            "AI has advanced rapidly in NLP, computer vision, and robotics, "
            "driving industry-wide adoption for automation and improved "
            "decision-making. However, concerns about job loss, privacy, "
            "and ethics have prompted global efforts to regulate AI."
        ),
        expected_output=(
            "AI has progressed significantly in areas like NLP, computer "
            "vision, and robotics, with widespread industry adoption. "
            "Concerns about job displacement, privacy, and ethics are "
            "leading to regulatory efforts worldwide."
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
            "Remote work surged post-pandemic, with many companies adopting "
            "hybrid models. While it boosts productivity and satisfaction, "
            "challenges like isolation and work-life balance remain. "
            "Companies are investing in tools and policies to help."
        ),
        expected_output=(
            "Since the pandemic, remote and hybrid work have grown. "
            "Benefits include higher productivity and satisfaction, but "
            "challenges like isolation and blurred work-life boundaries "
            "persist, prompting investment in digital solutions."
        ),
    ),
    LLMTestCase(
        input=(
            "The global push toward renewable energy has accelerated in "
            "response to climate change. Solar and wind power have become "
            "the fastest-growing energy sources, with costs declining "
            "significantly over the past decade. Many countries have set "
            "ambitious targets to achieve carbon neutrality by 2050. "
            "However, challenges remain in energy storage, grid "
            "infrastructure, and the transition from fossil fuels, "
            "which still account for a large portion of global energy "
            "production."
        ),
        actual_output=(
            "Renewable energy adoption is accelerating due to climate "
            "change, with solar and wind power leading growth and falling "
            "costs. Countries aim for carbon neutrality by 2050, but "
            "storage, grid, and fossil fuel transition challenges persist."
        ),
        expected_output=(
            "Climate change is driving rapid renewable energy growth, "
            "especially solar and wind. Many nations target carbon "
            "neutrality by 2050, though energy storage, grid upgrades, "
            "and fossil fuel dependence remain obstacles."
        ),
    ),
]


# ---------------------------------------------------------------------------
# Sample test cases: Japanese summarization
# ---------------------------------------------------------------------------

test_cases_ja = [
    LLMTestCase(
        input=(
            "日本の少子高齢化は深刻な社会問題となっています。出生率の低下と平均寿命の"
            "延びにより、労働人口が減少し、社会保障制度への負担が増大しています。"
            "政府は子育て支援策の拡充や外国人労働者の受け入れ拡大などの対策を講じて"
            "いますが、根本的な解決には至っていません。"
        ),
        actual_output=(
            "Japan faces a serious aging population and declining birthrate, "
            "leading to workforce shrinkage and increased social security "
            "burdens. Government measures including childcare support and "
            "foreign worker policies have not yet fundamentally resolved "
            "the issue."
        ),
        expected_output=(
            "Japan's declining birthrate and aging population are causing "
            "labor shortages and social security strain. Despite government "
            "efforts in childcare support and immigration, fundamental "
            "solutions remain elusive."
        ),
    ),
]


# ---------------------------------------------------------------------------
# Evaluation helpers
# ---------------------------------------------------------------------------

ALL_GEVAL_METRICS = [
    summarization_conciseness,
    summarization_faithfulness,
    summarization_coverage,
    summarization_coherence,
]

ALL_METRICS = [summarization_builtin] + ALL_GEVAL_METRICS


def evaluate_summarization_en(test_case: LLMTestCase) -> None:
    """Run all English summarization metrics against a single test case."""
    for metric in ALL_METRICS:
        assert_test(test_case, [metric])
