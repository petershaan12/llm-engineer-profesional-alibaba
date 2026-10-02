# Alibaba LLM Engineer Professional — Flashcard Instructions

## Goal

Create exactly 40 English practice questions **for each study category** (240 total) for Peter's preparation for the Alibaba Cloud LLM Engineer Professional certification. Peter previously failed the exam and needs serious practice that builds understanding, diagnoses mistakes, and strengthens weak areas. Save one 40-question JSON file for each category.

Use the lessons in this directory as the source of truth:

`/home/peter/aliyun_acp_learning/LLM_ACP_EN/p2_Build LLM Q&A System`

Read the relevant notebook explanations and code before writing questions. Use supporting files when necessary. Create original practice questions grounded in these materials; do not present them as official exam questions or claim that this set covers the entire certification syllabus.

## Previous performance and question allocation

This allocation prioritizes weak areas while retaining coverage of every section. It is a study plan, not an official exam weighting.

| Section | Previous performance | Questions | Primary lessons |
| --- | --- | --- | --- |
| LLM Application Development | 65% | 40 | 2.1 |
| Prompt Engineering | 50% | 40 | 2.3 |
| RAG | 50% | 40 | 2.2, 2.4, 2.5 |
| LLM Fine-tuning | 20% | 40 | 2.7 |
| Production Practices and AI Security | Unconfirmed: entered as "709" | 40 | 2.8, 2.9, 2.A |
| AI Agent and Applications | 65% | 40 | 2.6 |
| **Total** | | **240** | |

Do not silently convert "709" into 70%. Keep it unconfirmed until Peter clarifies it. Give each question one primary section so it is counted only once.

## Question formats

- Include both **Single Choice** and **Multiple Choice** throughout the set.
- Single Choice: exactly one correct option; use radio buttons in the flashcard interface.
- Multiple Choice: more than one correct option; use independent checkboxes. The only selection instruction should be **"Select all that apply."**
- **Never disclose or hint at the number of correct answers before submission.** Do not write "choose two," "three answers are correct," or similar wording. Do not enforce an exact selection count, display a required-count message, or disable submission based on the number of correct answers.
- Vary the number and positions of correct options across multiple-choice questions so they do not form a predictable pattern.
- Use four or five clearly labeled options. Make distractors plausible and based on realistic misunderstandings.
- Avoid "all of the above," "none of the above," ambiguous wording, overlapping options, and clues from option length or grammar.

## Coverage and difficulty

Include foundational, application, and challenging diagnosis or trade-off questions in every category. Difficulty should come from applying the lessons, not obscure trivia or trick wording.

Cover the following where supported by the source material:

- **LLM Application Development:** API calls, conversation history, streaming, temperature, and top_p.
- **Prompt Engineering:** clear instructions, delimiters, roles, output formats, few-shot examples, prompt iteration, AI judges, and prompting reasoning models.
- **RAG:** indexing and retrieval, embeddings, chunking, query rewriting, reranking, retrieval versus generation failures, and evaluation metrics such as context precision, context recall, and answer correctness.
- **LLM Fine-tuning:** choosing fine-tuning versus prompting or RAG, dataset quality and splits, loss and gradient descent, learning rate, epochs, batch size, sequence length, LoRA and rank, overfitting, evaluation, and adapter merging.
- **Production Practices and AI Security:** deployment choices, latency and cost, scaling and reliability, prompt injection, unsafe tool use, content guardrails, and knowledge-base access control. Include two questions on deployment/production and two on security.
- **AI Agent and Applications:** function calling, structured output validation, ReAct, MCP, workflow choices, reflection, memory, and evaluation.

Use realistic scenarios such as troubleshooting an employee Q&A bot, interpreting evaluation results, improving a fine-tuning run, or securing an agent. Include small code snippets or metric tables when they help test understanding. State the constraints needed to make the answer unambiguous.

## Required content for every flashcard

1. Unique ID from Q01 through Q40.
2. Primary section, difficulty, and question type.
3. Question and labeled answer options.
4. Correct option IDs, hidden until submission.
5. A clear explanation of why each correct option is correct.
6. A separate explanation of why each incorrect option is wrong and, where useful, when it would apply.
7. A short takeaway that explains the underlying principle.
8. A source reference with the exact relative notebook filename and relevant section heading. Include a cell index if a heading is insufficient to locate the evidence.

Keep answers, explanations, takeaways, and source references in the answer side of the card so they cannot give away the answer during the attempt. Never invent source references. Resolve unsupported or ambiguous claims by revising or replacing the question.

## Flashcard learning behavior

- Use a simple flashcard screen: lesson filter pills, one centered card, a card count and progress bar, previous/next controls, Reveal, and Shuffle.
- Show one question and its answer options on the front. Let Peter think or select options, then reveal the answer on the back. Multiple-choice cards must say only **"Select all that apply"** before reveal; never hint at the number of correct options.
- On the back, show the correct option IDs, why each option is right or wrong, the takeaway, and the notebook reference.
- Support keyboard navigation and keep the layout responsive. Keep study progress optional and local; do not put scores or dashboards ahead of the current card.

## Completion checks

Before delivering the question set, confirm that:

- There are exactly 40 unique questions in each of the six category files (240 total).
- Both question types are present; each answer key satisfies its type.
- Every answer and explanation is supported by a precise lesson reference.
- No question reveals the number of correct multiple-choice answers before submission.
- No duplicate or lightly reworded questions inflate the set.
- Explanations address every option and help Peter understand the mistake.
- The questions emphasize fine-tuning, prompt engineering, and RAG while preserving coverage of all six sections.
