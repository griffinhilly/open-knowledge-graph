---
id: web-gis
title: Web GIS
domain: earth-and-space-sciences
course: remote-sensing-and-gis
prerequisites:
- id: gis-fundamentals
  type: hard
- id: spatial-data-models
  type: soft
builds-toward: []
tags:
- web-gis
- web-mapping
- geospatial-web
- map-services
stage: advanced
status: validated
---

# Web GIS

## Core Idea
Web GIS extends geographic information systems to the web, enabling spatial data sharing, visualization, and analysis through browsers without requiring desktop GIS software. The architecture typically follows a client-server model: spatial data servers (GeoServer, ArcGIS Server, MapServer) host and process geospatial data, exposing it through standardized web services (WMS, WFS, WMTS, OGC API). Web clients (Leaflet, OpenLayers, Mapbox GL, ArcGIS JS API) render interactive maps in browsers. Cloud-native geospatial formats (Cloud-Optimized GeoTIFF, GeoParquet, PMTiles) enable direct access to large datasets without server-side processing. Web GIS has democratized access to geospatial information, enabling non-specialists to interact with spatial data.

## Questions

```yaml
- question: "A government agency wants to publish an interactive flood risk map that citizens can query by address. Which Web GIS architecture would serve this need?"
  type: multiple-choice
  options:
    - "Email PDF maps to all residents"
    - "A web mapping application with a tile base map, a WMS/WFS layer serving flood zone polygons from a spatial database, geocoding for address search, and identify/query tools for parcel-level flood risk information"
    - "Install desktop GIS software on every citizen's computer"
    - "A static image of the flood map posted on the agency website"
  answer: 1
  explanation: "This requires an interactive web application combining a base map for context, flood data served dynamically so it stays current, geocoding to convert addresses to map locations, and query capability to retrieve flood risk attributes for specific parcels. This architecture serves unlimited users through browsers without software installation or GIS expertise."

- question: "WMS (Web Map Service) and WFS (Web Feature Service) return the same type of data."
  type: true-false
  answer: false
  explanation: "WMS returns pre-rendered map images (PNG/JPEG) -- the client receives a picture and cannot query individual features. WFS returns the actual vector feature data (GML/GeoJSON) with geometry and attributes, allowing the client to query, filter, style, and analyze features. WMS is simpler and faster for display; WFS provides full data access for interactive applications. The choice depends on whether the client needs to just view or also interact with the data."

- question: "Explain what tile-based web mapping is and why it transformed web GIS performance."
  type: short-answer
  answer: "Tile-based mapping pre-renders the map at multiple zoom levels as grids of small image tiles (typically 256x256 pixels). Instead of rendering the entire map for each request, the server serves only the tiles visible in the current view extent, and clients cache tiles for reuse. This transformed performance because: (1) rendering is done once at build time, not per request; (2) only visible tiles are transferred, reducing bandwidth; (3) clients cache tiles locally, eliminating redundant requests; (4) tiles from different zoom levels enable smooth multi-scale navigation. Vector tiles extend this concept by serving pre-tiled vector data that clients render dynamically."
  explanation: "Tiling converts an impossibly expensive render-on-demand problem into a manageable serve-from-cache problem, enabling fluid map interaction that feels like panning across a continuous surface."
```

## Explainer

The evolution from desktop GIS to web GIS parallels the broader shift from installed software to web applications. Desktop GIS (ArcGIS Pro, QGIS) remains essential for complex analysis, data creation, and production cartography. But for data sharing, public engagement, field data collection, and collaborative workflows, web GIS has become the default delivery mechanism.

The server-side stack manages spatial data and processing. Spatial databases (PostGIS, SQL Server Spatial) store vector and raster data with spatial indexing for fast queries. Map servers (GeoServer, MapServer, ArcGIS Server) expose this data through OGC-standardized web services. Tile servers pre-render map tiles for fast base map delivery. Processing services expose geoprocessing tools (buffering, overlay, routing) as web APIs.

The client-side stack renders interactive maps in browsers. Libraries like Leaflet (lightweight, mobile-friendly), OpenLayers (full-featured, OGC-compliant), and Mapbox GL JS (vector tiles, 3D, WebGL-rendered) handle map display, user interaction, and data visualization. Modern web maps combine multiple tile and data layers, support client-side feature rendering and analysis, and integrate with web frameworks (React, Vue) for full application development.

The cloud-native geospatial movement is dissolving the server layer entirely. Cloud-Optimized GeoTIFF (COG) allows clients to request just the portion of a raster they need via HTTP range requests directly from cloud storage. GeoParquet provides efficient columnar storage for large vector datasets. PMTiles packages millions of map tiles into a single file accessible without a tile server. These formats enable serverless architectures where browsers access geospatial data directly from object storage, dramatically reducing infrastructure complexity and cost.
