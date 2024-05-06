---
title: 'MUSTANG-2 proposal tools'
tags:
  - Python
  - MUSTANG-2
  - GBT
authors:
  - name: Charles Romero
    orcid: 0000-0001-5725-0359
    affiliation: '1'
affiliations:
    - name: Harvard-Smithsonian Center for Astrophysics, 60 Garden St. Cambridge, MA 02134
      index: 1
date: 05 May 2024
bibliography: paper.bib
---

# Summary

MUSTANG-2 is a 215-detector array that was installed on the 100-m Robert C. Byrd Green Bank Telescope (GBT) in 2016. Observing at 90 GHz, with a continuum bandpass between 75 and 105 GHz, it achieves $10^{\prime\prime}$ resolution (FWHM) and has an instantaneous field of view (FOV) of $4^{\prime}.2$. The primary observing strategy employed for MUSTANG-2 observations is on-the-fly mapping with a Lissajous daisy pattern sufficiently large to go off-source. A fundamental reasons for this strategy is due to the data processing, which is itself a differencing measurement. In this research note, we provide some light-weight tools that may be useful for proposers of MUSTANG-2.
    
# Statement of need

MUSTANG-2 is a continuum camera operating on the GBT for which
mapping speeds have disseminated primarily as a single number calculated as the RMS within the central two arcminutes of a Lissajous daisy scan. However, the noise profile of MUSTANG-2 observations (for such scans) has a radial dependence (\autoref{fig:M2mappingSpeeds}). As such, proposers may wish to obtain results outside of the inner two arcminutes and potentially combine multiple scan pointings. Additionally, MUSTANG-2 has a published transfer function [@romero:2020], but this has largely not be incorporated into the technical justification of MUSTANG-2 proposals. This package provides a lightweight set of tools that allow MUSTANG-2 proposers to incorporate more advanced sensitivity maps and signal transmittance into their technical justifications.

![Mapping speeds profiles by scan radius (in arcminutes) for a single pointing.\label{fig:M2mappingSpeeds}](AverageMappingSpeedsTogether_M2homepage.png){ width=80% }

## Sensitivity Maps

While a single pointing on a target center can be sufficient, the MUSTANG-2 team has favored an offset scan strategy. This scan strategy employs four pointings which are offset (to the north, south, east, and west) of the target center. The offset can be specified; an offset of 1.5 arcminutes in each direction is typical. This provides a roughly uniform sensitivity in a central area larger than two arcminutes (see \autoref{fig:SimObs}) and reduces residual atmospheric noise.

This package simulates maps produced with the MIDAS pipeline [@romero:2020], which is the canonical pipeline for MUSTANG-2 data products. The default units for generated ``FITS`` files are Kelvin in the Rayleigh-Jeans approximation. Plotting routines in this package default to $\mu$K (Rayleigh-Jeans). Notes on converting from Compton $y$ or Jy/beam are provided in the documentation.

![**Left:** MUSTANG-2 sensitivity map (map of RMS), 20 hours on-source using both a single scan size and an offset pointing strategy.**Right:** WIKID sensitivity map for similar pointing strategy, but only 10 hours on source. \label{fig:SimObs}](M2_vs_WIKID_c.pdf){ width=100% }

## Filtering signal

Given the prevalence of projects targeting galaxy clusters via the Sunyaev-Zel'dovich [SZ; @sunyaev:1972] effect, we have included the ability to estimate the SZ effect from a spherical cluster which uses an universal pressure profile (UPP) as parameterized in [A10; @arnaud:2010]. Users may also supply their own (unfiltered) sky images. The package saves the filtered signal as a ``FITS`` file.

# Extension: WIKID

We include options to simulate observations with a potential successor to MUSTANG-2, WIKID [@dicker:2023]. WIKID is proposed to be a single band continuum camera with polarization capabilities and a field of view just over $8^{\prime}$. Mapping speed profiles and approximate transfer functions are derived using real MUSTANG-2 data and simulating observations, within MIDAS, for a WIKID array of detectors with improved detector sensitivity and reduced readout noise. \autoref{fig:SimObs} compares expected sensitivity maps for MUSTANG-2 and WIKID for the same pointing with only half the on-source times as with MUSTANG-2.

# Acknowledgements

This project uses the following Python packages: Astropy [@astropy:2022], NumPy [@numpy:2020]. The Green Bank Observatory is a facility of the National Science Foundation operated under cooperative agreement by Associated Universities, Inc.

# References