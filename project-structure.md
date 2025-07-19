```bash
zyro/
├── zyro/
│   ├── auth/  
│   │   ├── middleware.py
│   │   ├── utils.py
│   │   └── schemes.py
│   ├── core/                 # Core YAML parsing, route generation, runtime engine
│   │   ├── parser.py         # Parse config.yaml and structure logic
│   │   ├── router.py         # Dynamic FastAPI route injection
│   │   └── executor.py       # Handles raw/python/llm/task responses
│   │
│   ├── engines/              # Framework-specific logic (FastAPI engine)
│   │   └── fastapi_engine.py
│   │
│   ├── deployers/            # Deployment generators (Docker, AWS, Kubernetes)
│   │   ├── dockerizer.py
│   │   ├── aws_lambda.py
│   │   ├── k8s_generator.py
│   │   └── github_cicd.py
│   │
│   ├── logger/               # Structured logging system
│   │   └── log_manager.py
│   │
│   ├── validators/           # JSON Schema / Pydantic validators
│   │   ├── schema_loader.py
│   │   └── validator.py
│   │
│   ├── metrics/              # Health, metrics, Prometheus integration
│   │   └── metrics_collector.py
│   │
│   └── cli.py                # Main CLI tool (zyro run, zyro deploy...)
│
├── schemas/                  # Optional user-uploaded validation schemas
│   └── book_schema.json
│
├── tests/                    # Integration + auto-generated test cases
│   └── test_generated.py
│
├── Dockerfile                # Auto-generated from YAML
├── config.yaml               # User input that drives everything
└── README.md
```
