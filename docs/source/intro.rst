Introduction
============

``M2_ProposalTools`` is a high-level Python package intended to help proposers of MUSTANG-2 with their technical justification.
There are two fundamental aspects of technical justification at play:

#. Generating sensitivity maps, and
#. Filtering the astronomical signal.

The package is designed to work in :math:`\\mu` K (Rayleigh-Jeans). Users may supply a map (as a fits file) in these units.
If the user is proposing to observe galaxy clusters and it is sufficient to assume a spherical `A10 <https://ui.adsabs.harvard.edu/abs/2010A%26A...517A..92A/abstract>`_ model, then the user can
use tools in this package to simulate such a cluster model. Both the sensitivity and filtering aspects should be understood to be approximate.

The current implementation has been developed in Python 3 and tested on Python 3.6+ under Linux and Mac OS.

Motivation
**********

The MUSTANG-2 team has published mapping speed profiles for its canonical scanning types. However, it is helpful for proposers
to see how signal of extended sources is filtered and related to sensitivities for an adopted observing time and strategy. As noted
in papers such as `Dicker et al. (2020) <https://ui.adsabs.harvard.edu/abs/2020ApJ...902..144D/abstract>`_, we often employ a
strategy with offset pointings; this helps with noise removal in our data processing, but it means that our noise profiles aren't
those from a single pointing. This package provides tools for proposers to better understand a resultant sensitivity map.

Moreover, it also helps the user see how the signal will be filtered by standard (MIDAS) processing. MIDAS processed maps are the standard maps produced for MUSTANG-2 observers; they are portable and are delivered with an associated transfer function which allows the observer to perform forward modelling thereby recovering plausible models for their object. See, for instance `Romero et al. (2020) <https://ui.adsabs.harvard.edu/abs/2020ApJ...891...90R/abstract>`_ and `Andreon et al. (2021) <https://ui.adsabs.harvard.edu/abs/2021MNRAS.505.5896A/abstract>`_. 

Citation
********
A research note regarding this package is forthcoming. Citation information will be updated accordingly

Caveats and extensions
**********************

Note that this package is not concerned with Minkasi (e.g. `Romero et al. (2020) <https://ui.adsabs.harvard.edu/abs/2020ApJ...891...90R/abstract>`_) which can produce maps, but is best suited for directly fitting models in the time-domain. There are a multitude of reasons not to include this; two reasons dominate: (1) the Minkasi tool is not ready for public distribution, and (2) for the purposes of proposing, the framework using MIDAS is entirely sufficient.

On the note of model fitting, we have included tools to fit pressure profiles to a spherical cluster and estimate :math:`M_{500}` based on 
an `A10 <https://ui.adsabs.harvard.edu/abs/2010A%26A...517A..92A/abstract>`_ Y-M scaling relation. This is a fairly crude implementation and should serve only to get a (correspondingly) crude estimate of the uncertainties on a resultant mass estimation. 
