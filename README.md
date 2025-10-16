# QcrB Inhibition (M. tuberculosis)

The cytochrome bcc complex (QcrB) is a subunit of the mycobacterial cyt-bcc-aa3 oxidoreductase in the electron transport chain (ETC), and it has been suggested as a good M.tb target due to the bacterias dependence on oxidative phosphorylation for its growth. The authors use a dataset of 352 molecules, of which 277 are classified as active (QIM < 1 uM), 58 as moderately active ( 1 > QIM < 20 uM) and 78 as inactive (QIM > 20). Qim refers to quantification of intracellular mycobacteria.

This model was incorporated on 2023-04-06.


## Information
### Identifiers
- **Ersilia Identifier:** `eos24jm`
- **Slug:** `qcrb-tb`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `M.tuberculosis`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Class 1: active(QIM < 1uM), Class 2: moderately active (1 < QIM < 20uM), Class 3: inactive (QIM > 20uM)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| class | integer | low | Class 1: active(QIM < 1uM) - Class 2: moderately active (1 < QIM < 20uM) - Class 3: inactive (QIM > 20uM) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos24jm](https://hub.docker.com/r/ersiliaos/eos24jm)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24jm.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24jm.zip)

### Resource Consumption
- **Model Size (Mb):** `3`
- **Environment Size (Mb):** `791`
- **Image Size (Mb):** `762.27`

**Computational Performance (seconds):**
- 10 inputs: `30.68`
- 100 inputs: `20.74`
- 10000 inputs: `278.39`

### References
- **Source Code**: [https://github.com/CoutinhoLab/Q-TB/](https://github.com/CoutinhoLab/Q-TB/)
- **Publication**: [https://pubs.acs.org/doi/full/10.1021/acsomega.2c01613](https://pubs.acs.org/doi/full/10.1021/acsomega.2c01613)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [CC0-1.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos24jm
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos24jm
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
