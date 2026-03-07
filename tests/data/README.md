# Example data for SOMA

This folder contains example data for testing and demonstrating the datamodel,
sorted in subfolders:

- `valid` - Data conforming to the datamodel. Used to verify the datamodel.
- `invalid` - Data not conforming to the datamodel. Used to verify validation.
- `problem` - Data which are not yet handled correctly in the current schema version,
   again separated into valid/invalid.
- `valid_bkup` - Backup of previous test data (pre-microschema refactor).

## Schema Structure

The schema uses an **assay-centric architecture** with domain-specific assay classes.
All data files use the `Container` class as the root element.

### Assay Microschemas

| Assay Class | Description | Container Slot |
|-------------|-------------|----------------|
| CiliaryFunctionAssay | Ciliary beat frequency, active area, morphology | `ciliary_function_assays` |
| ASLAssay | Airway surface liquid height, PCL depth, ion composition | `asl_assays` |
| MucociliaryClearanceAssay | Mucociliary clearance and transport | `mcc_assays` |
| OxidativeStressAssay | ROS, lipid peroxidation, antioxidant capacity | `oxidative_stress_assays` |
| CFTRFunctionAssay | CFTR chloride secretion and function | `cftr_assays` |
| EGFRSignalingAssay | EGFR signaling and phosphorylation | `egfr_signaling_assays` |
| GobletCellAssay | Goblet cells, MUC5AC/MUC5B expression | `goblet_cell_assays` |
| BALFSputumAssay | BALF/sputum cell counts and cytokines | `balf_sputum_assays` |
| LungFunctionAssay | FEV1, FVC, spirometry outcomes | `lung_function_assays` |
| FoxJExpressionAssay | FoxJ1 expression and ciliogenesis | `foxj_assays` |
| GeneExpressionAssay | Target gene mRNA expression | `gene_expression_assays` |

### Supporting Entities

| Entity | Description | Container Slot |
|--------|-------------|----------------|
| Protocol | Detailed experimental procedures | `protocols` |
| Method | General measurement techniques | `methods` |
| KeyEvent | AOP key events | `key_events` |
| AdverseOutcomePathway | Complete AOP definitions | `adverse_outcome_pathways` |

## File Naming Convention

All example data files must conform to the scheme `Container-<descriptor>.yaml`
where `<descriptor>` is a descriptive name for the test case. The `Container` prefix
indicates the root class used for validation.
