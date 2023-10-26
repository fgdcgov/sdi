.. meta::
   :title: FGDC-STD-007.1-1998 Geospatial Positioning Accuracy Standards, Part 2: Standards for Geodetic Networks 
   :description: Part 1 applies to accuracy reporting for geodetic networks.
   :keywords: NSDI, geodetic, geospatial, standards, FGDC, CSDGM


FGDC-STD-007.1-1998 Standards for Geodetic Networks 
-------------------------------

Geospatial Positioning Accuracy Standards, Part 1: Standards for Geodetic Networks

Summary
-------------------------------

Part 2 applies to accuracy reporting for geodetic networks. Geodetic control surveys establish a basic control network (framework) from which supplemental surveying and mapping work. They are performed to accuracy that is far more rigorous and quality assurance standards than those for control surveys for general engineering, construction, topographic mapping, or cadastral purposes.

1. INTRODUCTION
-------------------------------

"This document provides a common methodology for reporting the  accuracy of horizontal coordinate values and vertical coordinate values  for clearly defined features where the location is represented by a single point coordinate: examples are survey monuments, such as brass disks  and rod marks; prominent landmarks, such as church spires, standpipes, radio towers, tall chimneys, and mountain peaks; and targeted photogrammetric control points.  It provides a means to directly compare the accuracy of coordinate values obtained by one method (e.g., a cartographically-derived value) with that obtained by another method (e.g., a Global Positioning System (GPS) geodetic network survey) for the same point.  It is increasingly important for users to not only know the coordinate values, but also the accuracy of those coordinate values, so users can decide which coordinate values represent the best estimate of the true value for their applications."


1.1 Objective
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities which collect or produce data coordinates include geodetic network and crustal motion surveys; national, regional, state, and county topographic mapping; bathymetric mapping and nautical charting; engineering, construction, and facilities management mapping and drawing; cadastral and boundary surveying; etc.   These activities support geospatial data applications  in areas such as transportation, community development, agriculture, emergency response, environmental management, and information technology.

This document is being developed in parts to address various activities.  Each data activity will apply the same general accuracy standard to develop a reporting classification scheme for its particular data.  The following parts have been submitted to date:

Part 2, STANDARDS FOR GEODETIC NETWORKS.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

Geodetic control surveys are usually performed to establish a basic control network (framework) from which supplemental surveying and mapping work, covered in other parts of this document, are performed.  Geodetic network surveys are distinguished by use of redundant, interconnected, permanently monumented control points that comprise the framework for the National Spatial Reference System (NSRS) or are often incorporated into the NSRS.    These surveys must be performed to far more rigorous accuracy and quality assurance standards than control surveys for general engineering, construction, or topographic mapping.  Geodetic network surveys included in the NSRS must be performed to meet automated data  recording, submission, project review, and least squares adjustment requirements established by the National Geodetic Survey  (NGS).  The lead agency is the Department of Commerce, National Oceanic and Atmospheric Administration, National Ocean Service, NGS; the responsible FGDC unit is the Federal Geodetic Control Subcommittee (FGCS)."

Part 3, NATIONAL STANDARD FOR SPATIAL DATA ACCURACY. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The National Standard for Spatial Data Accuracy (NSSDA) implements a testing and statistical methodology for positional accuracy of fully georeferenced maps and digital geospatial data, in either raster, point," "or vector format, derived from sources such as aerial photographs, satellite imagery, and ground surveys.  The NSRS is the framework that references positions to the national datums.  Positional accuracy of geodetically surveyed points in the National Spatial Reference System is reported according to Part 2, Standards for Geodetic Control Networks, Geospatial Positioning Accuracy Standards.    NSRS points may also be selected as an independent source of higher accuracy to test positional accuracy of maps and geospatial data according to the NSSDA.     The lead agency is the Department of the Interior, U.S. Geological Survey, National Mapping Division.  The responsible FGDC unit is the Subcommittee on Base Cartographic Data.

In addition, two other parts have been identified for inclusion in this document and are under development:

Part 4, ENGINEERING, CONSTRUCTION, AND FACILITIES MANAGEMENT.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

This part will provide accuracy standards for engineering surveys and maps used to support planning, design, construction, operation, maintenance, and management of facilities, installations, structures, transportation systems, and related projects.  It uses the NSSDA for accuracy testing and verification of fully georeferenced maps for A/E/C and Facility Management applications such as  preliminary site planning and reconnaissance mapping.   It will also provide guidance in developing positional accuracy specifications for geospatial data products, such as architectural and engineering drawings, construction site plans, regional master planning maps, and related Geographical Information Systems (GIS), Computer-Aided Drafting and Design (CADD), and Automated Mapping/Facility Management (AM/FM) products, that may not be referenced to a national datum and where accuracy is based on survey closure ratios or elevation differences.

The lead agency is the Department of Defense, U.S. Army Corps of Engineers.  The responsible FGDC unit is the Facilities Working Group.

Part 5, NAVIGATION CHARTS AND HYDROGRAPHIC SURVEYS.   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This part will specify minimum standards for hydrographic surveys so that hydrographic (sounding) data are sufficiently accurate and spatial uncertainty is adequately quantified for safe use  by mariners.  The accuracy of hydrographic surveying is highly dependent upon knowledge of tidal datum planes and the special accuracy requirements to support safe navigation.  This part will provide a standardized methodology for evaluating survey data and reporting resultant data quality through a standard statistical approach. It will be based on the recently revised International Hydrographic Organization (IHO) Standard for Hydrographic Surveys, which is in the final stages of review by the international community.    The lead agency is Department of Commerce, National Oceanic and Atmospheric Administration, National Ocean Service, Office of the Coast Survey.  The responsible FGDC subcommittee is the Bathymetric and Nautical Chart Subcommittee.

1.1.3      Applicability
-------------------------------

Use Geospatial Positioning Accuracy Standards to evaluate and report the positional accuracy of spatial data produced, revised, or disseminated by or for the Federal Government.  According to Executive Order 12906,  Coordinating Geographic Data Acquisition and Access: the National Spatial Data Infrastructure (Clinton, 1994, Sec. 4. Data Standards Activities, item d), “Federal agencies collecting or producing geospatial data, either directly or indirectly  (e.g. through

grants, partnerships, or contracts with other entities), shall ensure, prior to obligating funds for such activities, that data will be collected in a manner that meets all relevant standards adopted through the FGDC process.”

1.1.4      Related Standards
-------------------------------

1.1.4.1   FGDC Standards

The Spatial Data Transfer Standard (SDTS) (ANSI-NCITS, 1998) specifies that a data quality report accompany the data in a standard transfer.  Because the quality report will function in the assessment for fitness of use, it must also be obtainable in its entirety and separately from the actual data.  The quality report consists of five portions: lineage, positional accuracy, attribute accuracy, logical consistency, and completeness.   Positional accuracy reported according to Geospatial Positioning Accuracy Standards will be included in the data quality report.

Part 2, Data Quality Information, of Content Standards for Digital Geospatial Metadata (Federal Geographic Data Committee, 1998) adopts the five elements of data quality specified by SDTS. Consequently, positional accuracy reported according to Geospatial Positioning Accuracy Standards will be encoded in Metadata.

1.1.4.2   ISO Technical Committee (TC) 211 Geographic Information/Geomatics Standards

ISO Standard 15046-13, Geographic Information - Quality Principles defines a data quality model and identifies  positional accuracy as a data quality element and various subelements of positional accuracy.   It provides a means of measuring how well the data set maps geospatial phenomena according to its product specification.

ISO Standard 15046-14, Geographic Information - Quality  - Evaluation Procedures provides data quality evaluation models for both data producers and data users.   The procedures are used to determine data quality results consistent with the data quality model defined by ISO Standard 15046-13.   They establish a framework to report data quality results in metadata and when necessary, in a separate data quality report.

1.1.5      Standards Development Procedures

Part 2, Standards for Geodetic Networks and Part 3, National Standard for Spatial Data Accuracy (NSSDA) were originally developed independently.   Following the first public review of the NSSDA, in its previous version as National Cartographic Standards for Spatial Accuracy, the NSSDA was aligned with emerging standards from the Federal Geodetic Control Subcommittee (FGCS).   The FGCS has broad participation from various Federal agencies.  Noting how individual FGDC subcommittees and working groups were developing accuracy standards, the FGCS membership agreed to sponsor an FGDC standards project to compile the various accuracy standards into one document and minimize redundancies.   The FGDC Standards Working  Group has endorsed this approach.   This is the first FGDC standards project to integrate standards for various data themes and applications."

1.1.6 Maintenance Authority

The U.S. Department of Commerce, National Oceanic and Atmospheric Administration,
National Ocean Service, National Geodetic Survey, maintains Part 1, Reporting Methodology,
Geospatial Positioning Accuracy Standards for the Federal Geographic Data Committee. Address
questions concerning Part 1, Reporting Methodology, Geospatial Positioning Accuracy Standards
to: Director, National Geodetic Survey, NOAA, N/NGS, 1315 East-West Highway, Silver
Spring, Maryland 20910.
