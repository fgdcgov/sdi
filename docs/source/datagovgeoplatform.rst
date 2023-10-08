Data.gov and The GeoPlatform Metadata Recommendations
======================
This document provides best practices only and is not intended as policy that agencies must comply with, or for audit purposes. Including Guidelines for National Geospatial Data Assets (NGDA)

  1. INTRODUCTION
-------------------------------

1.1 Objective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Introduction

Metadata creation and management is a geospatial data management best practice. Metadata records document the who, what, why, where, when, and how of the resource (dataset or service) and provide context for data consumers as to the content, extent, quality, purpose, intended use, and limitations of the resource.

The Federal Geographic Data Committee (FGDC) has long promoted the creation of standardized geospatial metadata and recent legislation including the Foundations for Evidence-Based Policymaking Act (or OPEN Government Data Act, Pub.L. 115–435) and the Geospatial Data Act of 2018 (GDA) specify critical roles for metadata. The GDA requires Covered Agencies1 to “include standards for metadata for geospatial data, and other appropriate standards, including documenting geospatial data with the relevant metadata and making metadata available through the GeoPlatform.”2 Lead Covered Agencies3 are required to create and maintain “metadata for geospatial data within the National Geospatial Data Asset data theme.”4 The GDA establishes the GeoPlatform, which is required to “include metadata for all geospatial data collected by covered agencies, directly or indirectly.”5 Further, the GDA requires that metadata standards “to the maximum extent practicable, shall be consistent with international standards and protocols.”6

Documenting geospatial data resources robustly and in accord with national, and international, metadata standards is a data management and stewardship best practice based on the principles of FAIR:
  
  •	Findable
Machine-readable metadata are essential for automatic discovery of datasets and services
•	Accessible
Once the user finds the required data, they need to know how it can be accessed
•	Interoperable
The data needs to work reliably with other data, applications,or workflows for analysis, storage, and processing
•	Reusable
The metadata should be well-described so that data can be used to derive other data and replicated and/or combined in different settings.

Table 1-1. Best practice based on the principles of FAIR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
    :widths: 5 10
    :header-rows: 1
    :stub-columns: 1

    * - Dimension
      - Description
    * - Findable
      - Machine-readable metadata are essential for automatic discovery of datasets and services
    * - Accessible
      - Once the user finds the required data, they need to know how it can be accessed
    * - Interoperable
      - The data needs to work reliably with other data, applications,or workflows for analysis, storage, and processing
    * - Reusable
      - The metadata should be well-described so that data can be used to derive other data and replicated and/or combined in different settings.


The recommendations that follow are intended to support implementation of the GDA and support metadata publishers in developing rich metadata content that will enhance the discovery of resources within Data.gov and the GeoPlatform and enable the utility of the results within the GeoPlatform. Special attention is given to the use of standardized vocabularies when curating keywords, the incorporation of unique identifiers, and the documentation of geospatial web services. Consistent use of these metadata
