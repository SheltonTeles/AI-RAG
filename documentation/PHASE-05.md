# PHASE 05: EVALUATION AND TESTING

## 1. Overview

The fifth phase focuses on evaluating the RAG system using questions based on the selected China Jiliang University institutional documents.

The evaluation aims to examine whether the system can retrieve relevant information, generate answers consistent with the source material, and interpret follow-up questions using conversational context.

The experiments are exploratory and qualitative. They focus on selected scholarship-related questions and conversational scenarios rather than a large-scale statistical evaluation.

## 2. Evaluation Approach

The system was examined through three main aspects:

1. **Retrieval relevance:** Whether the retrieved document passages contain information relevant to the user's question.
2. **Answer correctness:** Whether the generated response is consistent with the information contained in the retrieved passages.
3. **Conversational context handling:** Whether the system can reformulate ambiguous follow-up questions using previous conversation messages.

The evaluation used selected questions about Type A and Type C scholarships, as well as follow-up questions requiring contextual interpretation.

## 3. Type A Scholarship Requirements

The first experiment examined whether the system could retrieve and explain the academic requirements for the Type A scholarship.

The initial question was:

> What are the academic requirements for applying for a Type A scholarship?

The system retrieved information describing the requirements for the three scholarship award categories.

The retrieved information included the following academic thresholds:

| Scholarship category | Required average score | Minimum individual subject score |
|---|---:|---:|
| First class | 90 or above | 80 |
| Second class | 80 to below 90 | 75 |
| Third class | 70 to below 80 | 70 |

Additional eligibility conditions were also identified in the retrieved material, including minimum credit requirements, attendance conditions, and restrictions concerning failed or make-up examinations and disciplinary violations.

The generated response presented the scholarship requirements using the retrieved institutional information.

This experiment provided an initial indication that the system could locate and communicate relevant scholarship provisions.

## 4. Type C Scholarship Requirements

A second experiment examined the system's ability to retrieve information about the Type C Inclusive Scholarship.

The question was:

> What are the eligibility requirements for the Type C inclusive scholarship?

The basic RAG implementation retrieved a passage identified as Article 9, page 141 of the source material.

The retrieved provision described requirements including:

- A previous academic-year average score of at least 70.
- No failed or make-up examinations.
- Attendance of at least 75%.
- No unexcused absences, lateness, or early departures.
- No violations of laws or university disciplinary regulations.

The generated answer was consistent with the retrieved scholarship provision.

This experiment demonstrated the system's ability to retrieve information from another scholarship category within the institutional document collection.

## 5. History-Aware Follow-up Question Evaluation

The next experiment examined whether conversation history could help the system interpret questions that depend on previous messages.

The initial question was:

> What are the academic requirements for applying for a Type A scholarship?

A follow-up question was then submitted:

> What is the minimum individual subject score required for that class?

The phrase "that class" was ambiguous when considered independently. However, the system used the previous conversation to reformulate the follow-up into a standalone retrieval query:

> What is the minimum individual subject score requirement for each category of the Type A scholarship?

The reformulated query enabled the retriever to identify the relevant scholarship information.

The generated response correctly presented the minimum individual subject scores for the three categories:

- First-class scholarship: 80.
- Second-class scholarship: 75.
- Third-class scholarship: 70.

This experiment illustrated how query reformulation can help preserve the meaning of follow-up questions in a conversational RAG system.

## 6. Context-Dependent Scenario Evaluation

An additional scenario was used to examine whether the system could apply retrieved scholarship requirements to a specific case.

The question was:

> If a student has an average score of 85 but one subject score of 74, would the student qualify for the second-class scholarship?

The system used the previous conversation to identify the relevant Type A second-class scholarship requirements.

The retrieved information specified that the average score must be at least 80 and below 90, while every individual subject must have a score of at least 75.

The generated response correctly concluded that the student would not satisfy the individual subject score requirement because 74 is below the required minimum of 75.

This experiment examined not only information retrieval but also the system's ability to apply retrieved rules to a specific scenario.

## 7. Retrieval Without Conversation History

To illustrate the importance of conversational context, a follow-up question was also submitted through the basic retrieval implementation without conversation history:

> What is the minimum individual subject score required for that class?

Without the previous discussion, the query did not identify the scholarship category or even the scholarship context.

The basic retrieval implementation returned examination-related material, and the generated response referred to a general examination passing threshold of 60%.

This response did not address the intended scholarship question.

The result illustrates a limitation of processing context-dependent questions without conversational information.

However, this experiment should be interpreted cautiously. The basic implementation used a retrieval parameter of `k=5`, whereas the history-aware implementation used `k=3`. Consequently, the two implementations were not evaluated under identical retrieval settings, and the observed difference cannot be attributed exclusively to conversation history.

## 8. Summary of Experimental Results

The exploratory experiments are summarised below.

| Test | Evaluation focus | Observed result |
|---|---|---|
| Type A scholarship query | Retrieval and answer correctness | Relevant scholarship requirements retrieved and presented |
| Type C scholarship query | Retrieval and answer correctness | Relevant eligibility provision retrieved and summarised |
| Type A follow-up query | Query reformulation | Ambiguous reference successfully reformulated |
| Scholarship scenario | Application of retrieved rules | Correctly identified that a score of 74 did not meet the 75-point minimum |
| Follow-up without history | Context handling | Retrieved unrelated examination information |

The experiments indicate that the prototype could answer the selected scholarship questions using relevant retrieved information. They also illustrate the potential benefit of query reformulation when processing conversational follow-up questions.

## 9. Limitations of the Evaluation

The evaluation has several limitations.

First, the experiments were conducted using a limited collection of institutional documents and a relatively small set of manually selected questions.

Second, the evaluation was qualitative. No large-scale benchmark, statistical analysis, or automated evaluation framework was used to measure retrieval relevance or answer correctness.

Third, the basic and history-aware implementations used different retrieval values (`k=5` and `k=3`, respectively). Therefore, their observed outputs do not constitute a controlled comparison of the effect of conversation history.

Additionally, the experiments did not systematically evaluate citation accuracy, cross-lingual retrieval performance, or the reliability of abstention when information is absent from the knowledge base.

## 10. Outcome of Phase 05

The exploratory evaluation demonstrated that the implemented RAG prototype could retrieve relevant scholarship provisions and generate answers consistent with the selected source material in the tested scenarios.

The conversational experiments also illustrated how history-aware query reformulation can help resolve ambiguous follow-up questions.

Nevertheless, broader testing and more controlled experiments are required before drawing general conclusions about the system's reliability and effectiveness.