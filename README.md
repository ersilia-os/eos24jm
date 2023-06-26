# QcrB Inhibition (M. tuberculosis)

The cytochrome bcc complex (QcrB) is a subunit of the mycobacterial cyt-bcc-aa3 oxidoreductase in the electron transport chain (ETC), and it has been suggested as a good M.tb target due to the bacteria's dependence on oxidative phosphorylation for its growth. The authors use a dataset of 352 molecules, of which 277 are classified as active (QIM < 1 uM), 58 as moderately active ( 1 > QIM < 20 uM) and 78 as inactive (QIM > 20). Qim refers to quantification of intracellular mycobacteria.

## Identifiers

* EOS model ID: `eos24jm`
* Slug: `qcrb-tb`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Other value`
* Output Type: `Integer`
* Output Shape: `Single`
* Interpretation: Class 1: active(QIM < 1uM), Class 2:moerately active (1 < QIM < 20uM), Class 3:inactive (QIM > 20uM)

## References

* [Publication](https://pubs.acs.org/doi/full/10.1021/acsomega.2c01613)
* [Source Code](https://github.com/CoutinhoLab/Q-TB/)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos24jm)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24jm.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos24jm) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/full/10.1021/acsomega.2c01613) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a CC license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!