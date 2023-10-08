Data.gov and The GeoPlatform Metadata Recommendations
======================
This document provides best practices only and is not intended as policy that agencies must comply with, or for audit purposes. Including Guidelines for National Geospatial Data Assets (NGDA)

1. INTRODUCTION
-------------------------------

1.1 Objective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Metadata creation and management is a geospatial data management best practice. Metadata records document the who, what, why, where, when, and how of the resource (dataset or service) and provide context for data consumers as to the content, extent, quality, purpose, intended use, and limitations of the resource.

The Federal Geographic Data Committee (FGDC) has long promoted the creation of standardized geospatial metadata and recent legislation including the Foundations for Evidence-Based Policymaking Act (or OPEN Government Data Act, Pub.L. 115–435) and the Geospatial Data Act of 2018 (GDA) specify critical roles for metadata. The GDA requires Covered Agencies1 to “include standards for metadata for geospatial data, and other appropriate standards, including documenting geospatial data with the relevant metadata and making metadata available through the GeoPlatform.”2 Lead Covered Agencies3 are required to create and maintain “metadata for geospatial data within the National Geospatial Data Asset data theme.”4 The GDA establishes the GeoPlatform, which is required to “include metadata for all geospatial data collected by covered agencies, directly or indirectly.”5 Further, the GDA requires that metadata standards “to the maximum extent practicable, shall be consistent with international standards and protocols.”6

Documenting geospatial data resources robustly and in accord with national, and international, metadata standards is a data management and stewardship best practice based on the principles of FAIR:

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

The recommendations that follow are intended to support implementation of the GDA and support metadata publishers in developing rich metadata content that will enhance the discovery of resources within Data.gov and the GeoPlatform and enable the utility of the results within the GeoPlatform. Special attention is given to the use of standardized vocabularies when curating keywords, the incorporation of unique identifiers, and the documentation of geospatial web services. Consistent use of these metadataelements will enhance the user experience by enabling data download, visualization, analysis, and custom map production within the GeoPlatform and other geographical information systems.

The document outlines best practices for creating geospatial metadata and specifies metadata content recommendations that support the discovery of National Geospatial Data Assets (NGDA) within Data.gov and the GeoPlatform. The document also serves as a complement to the Project Open Data Metadata Schema provided at resources.data.gov.

1.2. Metadata Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In accord with the GDA, covered agencies are required to provide metadata to the GeoPlatform (via Data.gov) for all geospatial data. Metadata must be produced using a geospatial metadata standard. The FGDC currently endorses the FGDC-authored Content Standard for Geospatial Metadata (CSDGM) and several ISO 19000 series metadata standards.

Data.gov can ingest CSDGM and ISO 19115/19139 metadata and transforms the CSDGM metadata to ISO 19115/19139. GeoPlatform ingests the ISO metadata from Data.gov.

The ISO 19000 metadata series provides data stewards several advantages. It is a modular set of standards that enables the compilation of metadata elements specific to your data resource: digital map, geodatabase, imagery, web service, etc. The ISO metadata series provides for the documentation of current geospatial data formats and applications. Following are the ISO geospatial metadata standards in the 19000 series:

Table 1-2. ISO Geospatial Metadata Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
    :widths: 5 10
    :header-rows: 1
    :stub-columns: 1

    * - Dimension
      - Description
    * - ISO 19115: Geographic Information – Metadata content standard
      - formatted using ISO/TS 19139:2007: Geographic information –– Metadata –– XML schema Note that FGDC has yet to endorse the 2019 update ISO/TS 19139-1:2019: Geographic information — XML schema implementation — Part 1: Encoding rules
    * - ISO 19115-1:2014 Geographic Information–– Metadata –– Part 1: Fundamentals –– Metadata content standard
      - formatted using ISO/TS 19115-3:2016 Geographic information –– Metadata –– Part 3: XML schema implementation for fundamental concepts
    * - ISO 19115-2:2019 Geographic information – Metadata – Part 2: Extensions for acquisition and processing
      - formatted using ISO/TS 19139-2:2012: Geographic information — Metadata — XML schema implementation — Part 2: Extensions for imagery and gridded data



The GDA and OMB Circular A-119 call for agencies to use voluntary consensus standards, such as those developed through ISO, in lieu of government-unique standards. The FGDC Steering Committee has approved an effort to establish a task team to evaluate and recommend a path forward for reestablishing a resourced and sustainable standards process. The goal is to meet the FGDC’s and agencies’ responsibilities related to standards under the GDA, A-16, and other relevant directives. This work will result in developing and updating a standards management process that can be used to establish metadata standards under the GDA.

This guidance is written using the element names, examples, and XPaths from the most current, ISO 19115-1, standard. However, it provides specific guidance for CSDGM implementation and for ISO 19115 implementation where it differs from ISO 19115-1.

How to Read and Use This Document
This document provides guidance specific to the creation of metadata intended for publication to Data.gov and the GeoPlatform. The recommendations were developed to improve data discovery and to facilitate the assessment and application of found resources. Metadata producers are encouraged to read the entire document in order and incorporate the recommendations into their own metadata production process.

Readers should be aware of the following document components:
