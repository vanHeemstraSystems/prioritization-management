``` mermaid
flowchart TD
    Start[Start] --> ProductiveQ{Are we doing anything?}
    
    %% Non-productive path
    ProductiveQ -->|No| NonProd[Non-productive task]
    NonProd --> WontDo[Priority: WONT_DO]
    WontDo --> NonWaste1[Waste Status: NON_WASTE]
    
    %% Productive path - first branch
    ProductiveQ -->|Yes| EffectiveQ{Are we doing<br/>the right thing?}
    
    %% Ineffective path
    EffectiveQ -->|No| Ineffective[Task is ineffective]
    Ineffective --> EfficientQ1{Are we doing<br/>the things right?}
    
    %% Ineffective but efficient path
    EfficientQ1 -->|Yes| EfficientIneffective[Task is efficient<br/>but ineffective]
    EfficientIneffective --> P4B[Priority: P4B]
    P4B --> Waste1[Waste Status: WASTE]
    
    %% Ineffective and inefficient path
    EfficientQ1 -->|No| InefficientIneffective[Task is inefficient<br/>and ineffective]
    InefficientIneffective --> P5A[Priority: P5]
    P5A --> Waste2[Waste Status: WASTE]
    
    %% Effective path
    EffectiveQ -->|Yes| Effective[Task is effective]
    Effective --> EfficientQ2{Are we doing<br/>the things right?}
    
    %% Effective and efficient path
    EfficientQ2 -->|Yes| EffectiveEfficient[Task is effective<br/>and efficient]
    EffectiveEfficient --> P4A[Priority: P4A]
    P4A --> NonWaste2[Waste Status: NON_WASTE]
    NonWaste2 --> ImportantQ{Are we doing<br/>the Important Thing?}
    
    %% Important path with new Urgency question
    ImportantQ -->|Yes| Important[Task is Important]
    Important --> UrgentQ1{Are we doing<br/>the urgent thing?}
    
    %% Important + Urgent path
    UrgentQ1 -->|Yes| P1[Priority: P1]
    P1 --> NonWaste5[Waste Status: NON_WASTE]
    
    %% Important + Non-urgent path
    UrgentQ1 -->|No| P2B[Priority: P2.B]
    P2B --> NonWaste6[Waste Status: NON_WASTE]
    
    %% Unimportant path with Urgency question
    ImportantQ -->|No| Unimportant[Task is Unimportant]
    Unimportant --> UrgentQ2{Are we doing<br/>the urgent thing?}
    
    %% Unimportant + Urgent path
    UrgentQ2 -->|Yes| P2A[Priority: P2.A]
    P2A --> NonWaste3[Waste Status: NON_WASTE]
    
    %% Unimportant + Non-urgent path
    UrgentQ2 -->|No| P3[Priority: P3]
    P3 --> NonWaste4[Waste Status: NON_WASTE]
    
    %% Effective but inefficient path
    EfficientQ2 -->|No| EffectiveInefficient[Task is effective<br/>but inefficient]
    EffectiveInefficient --> P5B[Priority: P5]
    P5B --> Waste3[Waste Status: WASTE]
    
    %% All paths converge to Finish
    NonWaste1 --> Finish[Finish]
    Waste1 --> Finish
    Waste2 --> Finish
    NonWaste5 --> Finish
    NonWaste6 --> Finish
    NonWaste3 --> Finish
    NonWaste4 --> Finish
    Waste3 --> Finish
    
    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px
    classDef question fill:#f8e5ff,stroke:#333,stroke-width:2px
    classDef status fill:#e5efff,stroke:#333,stroke-width:1px
    classDef priority fill:#e5ffe8,stroke:#333,stroke-width:1px
    classDef waste fill:#ffe5e5,stroke:#333,stroke-width:1px
    classDef finish fill:#f9f9f9,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
    
    class ProductiveQ,EffectiveQ,EfficientQ1,EfficientQ2,ImportantQ,UrgentQ1,UrgentQ2 question
    class NonProd,Ineffective,EfficientIneffective,InefficientIneffective,Effective,EffectiveEfficient,EffectiveInefficient,Important,Unimportant status
    class WontDo,P4A,P4B,P5A,P5B,P2A,P2B,P3,P1 priority
    class Waste1,Waste2,Waste3,NonWaste1,NonWaste2,NonWaste3,NonWaste4,NonWaste5,NonWaste6 waste
    class Finish finish
```
