# Examples

This page provides comprehensive examples of using the Outcomes Working Group Data Model.
All examples use the `Container` class as the root element and demonstrate real-world
use cases for environmental health research data.

## Quick Start

The simplest way to get started is to pick an example that matches your measurement type
and adapt it to your data. Each example shows:

- Required fields for the measurement type
- Proper use of ontology-backed units
- Context for in vitro (cell culture) or in vivo (human/animal) settings

---

## In Vitro Measurements

These examples demonstrate measurements performed on cell culture systems, using the
`InVitroContext` mixin which provides the `cell_culture_system` slot for detailed
culture system specification.

### Ciliary Function Measurement

Measuring ciliary beat frequency (CBF) in primary human bronchial epithelial cells
cultured at air-liquid interface:

```yaml
ciliary_measurements:
  CILIARY:001:
    id: "CILIARY:001"
    name: "CBF measurement after ozone exposure"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "8.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_method: "high-speed video microscopy"
    measurement_date: "2024-01-15"
    cell_culture_system:
      id: "owg:culture-001"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

**Key points:**

- `observation_type` uses the `CiliaryObservationTypeEnum` (e.g., `ciliary_beat_frequency`, `ciliary_beat_pattern`, `percent_motile_cilia`)
- `cell_culture_system` is now a structured object with culture details
- `days_at_differentiation` indicates maturation time at ALI

---

### Airway Surface Liquid (ASL) Measurement

Measuring ASL height using micro-optical coherence tomography:

```yaml
asl_measurements:
  ASL:001:
    id: "ASL:001"
    name: "Airway surface liquid height"
    observation_type: asl_height
    quantity_measured:
      value: "7.2"
      unit:
        id: "UO:0000017"
        name: "micrometer"
    measurement_method: "micro-optical coherence tomography"
    measurement_date: "2024-02-10"
    cell_culture_system:
      id: "owg:culture-002"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28
```

---

### Mucociliary Clearance (MCC) Measurement

Tracking fluorescent microsphere transport rate:

```yaml
mcc_measurements:
  MCC:001:
    id: "MCC:001"
    name: "Mucociliary transport rate"
    observation_type: mucociliary_transport_rate
    quantity_measured:
      value: "45.3"
      unit:
        id: "UO:0000103"
        name: "micrometer per second"
    measurement_method: "fluorescent microsphere tracking"
    measurement_date: "2024-03-05"
    cell_culture_system:
      id: "owg:culture-003"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

### Oxidative Stress Measurement

Measuring reactive oxygen species (ROS) after PM2.5 exposure:

```yaml
oxidative_stress_measurements:
  OX:001:
    id: "OX:001"
    name: "ROS level after PM2.5 exposure"
    observation_type: reactive_oxygen_species
    quantity_measured:
      value: "2.5"
      unit:
        id: "UO:0000193"
        name: "fold change"
    measurement_method: "DCFDA fluorescence assay"
    measurement_date: "2024-01-20"
    cell_culture_system:
      id: "owg:culture-004"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 21
```

---

### CFTR Function Measurement

Measuring CFTR-mediated chloride secretion using Ussing chambers:

```yaml
cftr_measurements:
  CFTR:001:
    id: "CFTR:001"
    name: "CFTR chloride secretion"
    observation_type: cftr_chloride_secretion
    quantity_measured:
      value: "15.2"
      unit:
        id: "UO:0000274"
        name: "microampere per square centimeter"
    measurement_method: "Ussing chamber"
    measurement_date: "2024-04-12"
    cell_culture_system:
      id: "owg:culture-005"
      name: "Primary HBE ALI culture"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
      passage_number: 2
    days_at_differentiation: 28
```


## In Vivo Measurements

These examples demonstrate measurements from human or animal subjects, using the
`InVivoContext` mixin which provides participant and sample information.

### Lung Function Measurement

Spirometry measurement from a human subject:

```yaml
lung_function_measurements:
  LF:001:
    id: "LF:001"
    name: "FEV1 measurement"
    observation_type: fev1
    quantity_measured:
      value: "82.5"
      unit:
        id: "UO:0000187"
        name: "percent predicted"
    measurement_method: "Spirometry"
    measurement_date: "2024-08-10"
    participant:
      id: "PARTICIPANT:002"
      name: "Subject B"
```

**Key points:**

- `participant` replaces `cell_culture_system` for in vivo context
- No `days_at_differentiation` since this is a human measurement

---

### BALF/Sputum Measurement

Inflammatory cell differential from induced sputum:

```yaml
balf_sputum_measurements:
  BALF:001:
    id: "BALF:001"
    name: "Neutrophil percentage in induced sputum"
    observation_type: neutrophil_percentage
    quantity_measured:
      value: "45.0"
      unit:
        id: "UO:0000187"
        name: "percent"
    measurement_method: "Cytospin differential count"
    measurement_date: "2024-07-22"
    sample_type: sputum
    participant:
      id: "PARTICIPANT:001"
      name: "Subject A"
```

---

## Protocols, Methods, and Assays

The schema supports detailed documentation of experimental procedures through a
three-level hierarchy.

### Protocol Definition

A detailed protocol for CBF measurement:

```yaml
protocols:
  PROTOCOL:001:
    id: "PROTOCOL:001"
    name: "High-speed video microscopy for CBF"
    description: "Protocol for measuring ciliary beat frequency using high-speed video microscopy"
    study_context: in_vitro
    imaging_frame_rate:
      value: "200"
      unit:
        id: "UO:0000106"
        name: "hertz"
    imaging_duration:
      value: "2"
      unit:
        id: "UO:0000010"
        name: "second"
    temperature_control:
      value: "37"
      unit:
        id: "UO:0000027"
        name: "degree Celsius"
    replicate_count: 3
```

**Protocol slots include:**

- `imaging_frame_rate`, `imaging_duration`, `spatial_resolution` - for imaging protocols
- `temperature_control`, `humidity_control` - environmental conditions
- `detection_method`, `staining_type`, `antibody_used` - detection details
- `normalization_method`, `quality_control_criteria` - data processing

---

### Method Definition

A general measurement method:

```yaml
methods:
  METHOD:001:
    id: "METHOD:001"
    name: "High-speed video microscopy"
    description: "Video-based measurement of ciliary dynamics"
```

---

### Assay Definition

An assay type reference:

```yaml
assays:
  ASSAY:001:
    id: "OBI:0002119"
    name: "Ciliary beat frequency assay"
    description: "Assay to measure the frequency of ciliary beating"
```

---

## Cell Culture System Details

The updated schema provides rich detail for cell culture systems. Here's a comprehensive
example showing all available fields:

### Detailed 2D Cell Culture (ALI)

```yaml
cell_culture_system:
  id: "owg:detailed-ali-culture"
  name: "Primary HBE ALI culture from healthy donor"
  description: "Well-differentiated ALI culture for toxicant testing"
  cell_culture_growth_mode: air_liquid_interface
  substrate_type: transwell_insert
  passage_number: 2
  cell_line:
    id: "CLO:0000001"
    name: "Primary HBE cells"
    tissue_origin: "bronchus"
    disease_state: "normal"
    supplier: "Lonza"
    catalog_number: "CC-2540"
    authentication_method: "STR profiling"
    mycoplasma_status: "negative"
  culture_conditions:
    id: "owg:conditions-001"
    name: "Standard ALI conditions"
    days_at_air_liquid_interface: 21
    passage_number: 2
    substrate_type: transwell_insert
    cell_culture_growth_mode: air_liquid_interface
    donor_count: 3
    replicates_per_donor: 4
  culture_media:
    id: "owg:media-001"
    name: "PneumaCult-ALI Medium"
    base_medium: "PneumaCult-ALI"
    manufacturer: "STEMCELL Technologies"
    catalog_number: "05001"
```

### 3D Cell Culture (Organoid)

```yaml
cell_culture_system:
  id: "owg:lung-organoid"
  name: "Human lung organoid"
  cell_culture_growth_mode: organoid
  three_d_architecture: organoid
  matrix_composition: "Matrigel"
  organoid_type: "lung"
  size_range:
    min_value:
      value: "200"
      unit:
        id: "UO:0000017"
        name: "micrometer"
    max_value:
      value: "500"
      unit:
        id: "UO:0000017"
        name: "micrometer"
```

---

## Complete Container Example

Here's a complete example showing multiple measurement types in a single container:

```yaml
# Complete study data container
ciliary_measurements:
  CILIARY:001:
    id: "CILIARY:001"
    name: "CBF baseline"
    observation_type: ciliary_beat_frequency
    quantity_measured:
      value: "12.5"
      unit:
        id: "UO:0000106"
        name: "hertz"
    measurement_method: "high-speed video microscopy"
    measurement_date: "2024-01-15"
    cell_culture_system:
      id: "owg:culture-001"
      name: "Primary HBE ALI"
      cell_culture_growth_mode: air_liquid_interface
      substrate_type: transwell_insert
    days_at_differentiation: 21

protocols:
  PROTOCOL:001:
    id: "PROTOCOL:001"
    name: "CBF measurement protocol"
    study_context: in_vitro
    imaging_frame_rate:
      value: "200"
      unit:
        id: "UO:0000106"
        name: "hertz"
    temperature_control:
      value: "37"
      unit:
        id: "UO:0000027"
        name: "degree Celsius"
```

## Next Steps

- Browse the complete [Schema Documentation](elements/index.md) for all available classes and slots
- Read [About](about.md) to learn more about the project goals
- Visit the [GitHub Repository](https://github.com/EHS-Data-Standards/outcomes-working-group) to contribute
