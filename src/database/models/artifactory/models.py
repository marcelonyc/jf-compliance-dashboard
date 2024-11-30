# generated by datamodel-codegen:
#   filename:  response.json
#   timestamp: 2024-11-12T20:59:45+00:00

from __future__ import annotations


from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Boolean,
)
from database.database import metadata, json_type

local_item_table = Table(
    "local_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("key", String),
    Column("packageType", String),
    Column("description", String),
    Column("notes", String),
    Column("includesPattern", String),
    Column("excludesPattern", String),
    Column("repoLayoutRef", String),
    Column("signedUrlTtl", Integer),
    Column("priorityResolution", Boolean),
    Column(
        "environments", json_type
    ),  # This should be a relationship in a real model
    Column("blackedOut", Boolean),
    Column(
        "propertySets", json_type
    ),  # This should be a relationship in a real model
    Column("archiveBrowsingEnabled", Boolean),
    Column("xrayDataTtl", Integer),
    Column("downloadRedirect", Boolean),
    Column("cdnRedirect", Boolean),
    Column("xrayIndex", Boolean),
    Column("rclass", String),
    Column("projectKey", String),
    Column("forceNugetAuthentication", Boolean),
    Column("enableNormalizedVersion", Boolean),
    Column("maxUniqueSnapshots", Integer),
    Column("debianTrivialLayout", Boolean),
    Column("ddebSupported", Boolean),
    Column(
        "optionalIndexCompressionFormats", json_type
    ),  # This should be a relationship in a real model
    Column("checksumPolicyType", String),
    Column("handleReleases", Boolean),
    Column("handleSnapshots", Boolean),
    Column("snapshotVersionBehavior", String),
    Column("suppressPomConsistencyChecks", Boolean),
    Column("dockerApiVersion", String),
    Column("blockPushingSchema1", Boolean),
    Column("maxUniqueTags", Integer),
    Column("dockerTagRetention", Integer),
    Column("encryptStates", Boolean),
    Column("cargoAnonymousAccess", Boolean),
    Column("cargoInternalIndex", Boolean),
    Column("forceConanAuthentication", Boolean),
    Column("terraformType", String),
    Column("enableComposerV1Indexing", Boolean),
    Column("calculateYumMetadata", Boolean),
    Column("enableFileListsIndexing", Boolean),
    Column("yumRootDepth", Integer),
    Column("yumGroupFileNames", String),
)

remote_item_table = Table(
    "remote_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("key", String),
    Column("packageType", String),
    Column("description", String),
    Column("notes", String),
    Column("includesPattern", String),
    Column("excludesPattern", String),
    Column("repoLayoutRef", String),
    Column("signedUrlTtl", Integer),
    Column("priorityResolution", Boolean),
    Column(
        "environments", json_type
    ),  # This should be a relationship in a real model
    Column("url", String),
    Column("username", String),
    Column("password", String),
    Column("disableProxy", Boolean),
    Column("hardFail", Boolean),
    Column("offline", Boolean),
    Column("blackedOut", Boolean),
    Column("storeArtifactsLocally", Boolean),
    Column("socketTimeoutMillis", Integer),
    Column("localAddress", String),
    Column("retrievalCachePeriodSecs", Integer),
    Column("assumedOfflinePeriodSecs", Integer),
    Column("missedRetrievalCachePeriodSecs", Integer),
    Column("metadataRetrievalTimeoutSecs", Integer),
    Column("unusedArtifactsCleanupPeriodHours", Integer),
    Column("shareConfiguration", Boolean),
    Column("synchronizeProperties", Boolean),
    Column(
        "propertySets", json_type
    ),  # This should be a relationship in a real model
    Column("archiveBrowsingEnabled", Boolean),
    Column("listRemoteFolderItems", Boolean),
    Column("allowAnyHostAuth", Boolean),
    Column("enableCookieManagement", Boolean),
    Column("propagateQueryParams", Boolean),
    Column("blockMismatchingMimeTypes", Boolean),
    Column("mismatchingMimeTypesOverrideList", String),
    Column("bypassHeadRequests", Boolean),
    Column("disableUrlNormalization", Boolean),
    Column(
        "contentSynchronisation", json_type
    ),  # This should be a relationship in a real model
    Column("sendContext", Boolean),
    Column("passThrough", Boolean),
    Column("curated", Boolean),
    Column("retrieveSha256FromServer", Boolean),
    Column("xrayDataTtl", Integer),
    Column("downloadRedirect", Boolean),
    Column("xrayIndex", Boolean),
    Column("rclass", String),
    Column("handleReleases", Boolean),
    Column("handleSnapshots", Boolean),
    Column("suppressPomConsistencyChecks", Boolean),
    Column("remoteRepoChecksumPolicyType", String),
    Column("fetchJarsEagerly", Boolean),
    Column("fetchSourcesEagerly", Boolean),
    Column("maxUniqueSnapshots", Integer),
    Column("rejectInvalidJars", Boolean),
    Column("vcsType", String),
    Column("composerRegistryUrl", String),
    Column("vcsGitProvider", String),
    Column("pyPIRegistryUrl", String),
    Column("pyPIRepositorySuffix", String),
    Column("externalDependenciesEnabled", Boolean),
    Column(
        "externalDependenciesPatterns", json_type
    ),  # This should be a relationship in a real model
    Column("projectKey", String),
    Column("forceNugetAuthentication", Boolean),
    Column("enableNormalizedVersion", Boolean),
    Column("downloadContextPath", String),
    Column("feedContextPath", String),
    Column("v3FeedUrl", String),
    Column("symbolServerUrl", String),
    Column("dockerApiVersion", String),
    Column("blockPushingSchema1", Boolean),
    Column("dockerProjectId", String),
    Column("enableTokenAuthentication", Boolean),
    Column("forceConanAuthentication", Boolean),
    Column("terraformRegistryUrl", String),
    Column("terraformProvidersUrl", String),
    Column("ddebSupported", Boolean),
    Column("cargoAnonymousAccess", Boolean),
    Column("cargoInternalIndex", Boolean),
    Column("gitRegistryUrl", String),
    Column("remoteRepoLayoutRef", String),
    Column("podsCdnUrl", String),
    Column("podsSpecsRepoUrl", String),
    Column("podsForceModifyIndex", Boolean),
    Column("forceP2Authentication", Boolean),
)

virtual_item_table = Table(
    "virtual_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("key", String),
    Column("packageType", String),
    Column("description", String),
    Column("notes", String),
    Column("includesPattern", String),
    Column("excludesPattern", String),
    Column("repoLayoutRef", String),
    Column("signedUrlTtl", Integer),
    Column(
        "environments", json_type
    ),  # This should be a relationship in a real model
    Column(
        "repositories", json_type
    ),  # This should be a relationship in a real model
    Column("hideUnauthorizedResources", Boolean),
    Column("artifactoryRequestsCanRetrieveRemoteArtifacts", Boolean),
    Column("externalDependenciesEnabled", Boolean),
    Column(
        "externalDependenciesPatterns", json_type
    ),  # This should be a relationship in a real model
    Column("virtualRetrievalCachePeriodSecs", Integer),
    Column("rclass", String),
    Column("defaultDeploymentRepo", String),
    Column("keyPair", String),
    Column("pomRepositoryReferencesCleanupPolicy", String),
    Column("forceMavenAuthentication", Boolean),
    Column("projectKey", String),
    Column("forceNugetAuthentication", Boolean),
    Column("enableNormalizedVersion", Boolean),
    Column("dockerApiVersion", String),
    Column("resolveDockerTagsByTimestamp", Boolean),
    Column("cachingLocalForeignLayersEnabled", Boolean),
    Column("externalDependenciesRemoteRepo", String),
    Column("forceConanAuthentication", Boolean),
    Column("useNamespaces", Boolean),
    Column("ddebSupported", Boolean),
    Column("debianDefaultArchitectures", String),
    Column(
        "optionalIndexCompressionFormats", json_type
    ),  # This should be a relationship in a real model
    Column("forceP2Authentication", Boolean),
    Column(
        "p2Urls", json_type
    ),  # This should be a relationship in a real model
)

federated_item_table = Table(
    "federated_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("key", String),
    Column("packageType", String),
    Column("description", String),
    Column("notes", String),
    Column("includesPattern", String),
    Column("excludesPattern", String),
    Column("repoLayoutRef", String),
    Column("signedUrlTtl", Integer),
    Column("priorityResolution", Boolean),
    Column(
        "environments", json_type
    ),  # This should be a relationship in a real model
    Column("checksumPolicyType", String),
    Column("handleReleases", Boolean),
    Column("handleSnapshots", Boolean),
    Column("maxUniqueSnapshots", Integer),
    Column("snapshotVersionBehavior", String),
    Column("suppressPomConsistencyChecks", Boolean),
    Column("blackedOut", Boolean),
    Column(
        "propertySets", json_type
    ),  # This should be a relationship in a real model
    Column("archiveBrowsingEnabled", Boolean),
    Column(
        "members", json_type
    ),  # This should be a relationship in a real model
    Column("disableProxy", Boolean),
    Column("downloadRedirect", Boolean),
    Column("cdnRedirect", Boolean),
    Column("xrayIndex", Boolean),
    Column("xrayDataTtl", Integer),
    Column("rclass", String),
    Column("debianTrivialLayout", Boolean),
    Column("ddebSupported", Boolean),
    Column(
        "optionalIndexCompressionFormats", json_type
    ),  # This should be a relationship in a real model
    Column("projectKey", String),
    Column("forceNugetAuthentication", Boolean),
    Column("enableNormalizedVersion", Boolean),
    Column("dockerApiVersion", String),
    Column("blockPushingSchema1", Boolean),
    Column("maxUniqueTags", Integer),
    Column("dockerTagRetention", Integer),
)

release_bundle_item_table = Table(
    "release_bundle_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("key", String),
    Column("packageType", String),
    Column("description", String),
    Column("notes", String),
    Column("includesPattern", String),
    Column("excludesPattern", String),
    Column("repoLayoutRef", String, nullable=True),
    Column("signedUrlTtl", Integer),
    Column("priorityResolution", Boolean),
    Column(
        "environments", json_type
    ),  # This should be a relationship in a real model
    Column("blackedOut", Boolean),
    Column(
        "propertySets", json_type
    ),  # This should be a relationship in a real model
    Column("archiveBrowsingEnabled", Boolean),
    Column("xrayDataTtl", Integer),
    Column("downloadRedirect", Boolean),
    Column("cdnRedirect", Boolean),
    Column("xrayIndex", Boolean),
    Column("rclass", String),
)