## Add your own just recipes here. This is imported by the main justfile.

# Run the YAML-to-Excel pipeline test on example data
[group('model development')]
pipeline-test:
  mkdir -p tmp
  uv run linkml-validate -s src/soma/schema/soma.yaml tests/data/valid/Container-liu2024-pm25-cftr.yaml
  uv run python scripts/yaml_to_excel.py --input tests/data/valid/Container-liu2024-pm25-cftr.yaml --output tmp/Liu2024_pipeline_test.xlsx
  uv run linkml-validate -s src/soma/schema/soma.yaml tests/data/valid/Container-montgomery2020-pm25-mucociliary.yaml
  uv run python scripts/yaml_to_excel.py --input tests/data/valid/Container-montgomery2020-pm25-mucociliary.yaml --output tmp/Montgomery2020_pipeline_test.xlsx
  @echo "Pipeline test completed. Output in tmp/"
