"""init

Revision ID: 81f81659d733
Revises: 
Create Date: 2024-11-18 15:18:32.402438

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.sqlite import JSON
import os

os.environ["RUN_MODE"] = "alembic"
from src.config.app_config import get_settings

app_config = get_settings()
db_type = "postgresql"
if "sqlite" in app_config.db_url:
    db_type = "sqlite"

# revision identifiers, used by Alembic.
revision: str = "81f81659d733"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    if db_type == "sqlite":
        json_type = JSON
    else:
        json_type = JSONB

    op.create_table(
        "local_item",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("packageType", sa.String),
        sa.Column("description", sa.String),
        sa.Column("notes", sa.String),
        sa.Column("includesPattern", sa.String),
        sa.Column("excludesPattern", sa.String),
        sa.Column("repoLayoutRef", sa.String),
        sa.Column("signedUrlTtl", sa.Integer),
        sa.Column("priorityResolution", sa.Boolean),
        sa.Column(
            "environments", json_type
        ),  # This should be a relationship in a real model
        sa.Column("blackedOut", sa.Boolean),
        sa.Column(
            "propertySets", json_type
        ),  # This should be a relationship in a real model
        sa.Column("archiveBrowsingEnabled", sa.Boolean),
        sa.Column("xrayDataTtl", sa.Integer),
        sa.Column("downloadRedirect", sa.Boolean),
        sa.Column("cdnRedirect", sa.Boolean),
        sa.Column("xrayIndex", sa.Boolean),
        sa.Column("rclass", sa.String),
        sa.Column("projectKey", sa.String),
        sa.Column("forceNugetAuthentication", sa.Boolean),
        sa.Column("enableNormalizedVersion", sa.Boolean),
        sa.Column("maxUniqueSnapshots", sa.Integer),
        sa.Column("debianTrivialLayout", sa.Boolean),
        sa.Column("ddebSupported", sa.Boolean),
        sa.Column(
            "optionalIndexCompressionFormats", json_type
        ),  # This should be a relationship in a real model
        sa.Column("checksumPolicyType", sa.String),
        sa.Column("handleReleases", sa.Boolean),
        sa.Column("handleSnapshots", sa.Boolean),
        sa.Column("snapshotVersionBehavior", sa.String),
        sa.Column("suppressPomConsistencyChecks", sa.Boolean),
        sa.Column("dockerApiVersion", sa.String),
        sa.Column("blockPushingSchema1", sa.Boolean),
        sa.Column("maxUniqueTags", sa.Integer),
        sa.Column("dockerTagRetention", sa.Integer),
        sa.Column("encryptStates", sa.Boolean),
        sa.Column("cargoAnonymousAccess", sa.Boolean),
        sa.Column("cargoInternalIndex", sa.Boolean),
        sa.Column("forceConanAuthentication", sa.Boolean),
        sa.Column("terraformType", sa.String),
        sa.Column("enableComposerV1Indexing", sa.Boolean),
        sa.Column("calculateYumMetadata", sa.Boolean),
        sa.Column("enableFileListsIndexing", sa.Boolean),
        sa.Column("yumRootDepth", sa.Integer),
        sa.Column("yumGroupFileNames", sa.String),
    )

    op.create_table(
        "remote_item",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("packageType", sa.String),
        sa.Column("description", sa.String),
        sa.Column("notes", sa.String),
        sa.Column("includesPattern", sa.String),
        sa.Column("excludesPattern", sa.String),
        sa.Column("repoLayoutRef", sa.String),
        sa.Column("signedUrlTtl", sa.Integer),
        sa.Column("priorityResolution", sa.Boolean),
        sa.Column(
            "environments", json_type
        ),  # This should be a relationship in a real model
        sa.Column("url", sa.String),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String),
        sa.Column("disableProxy", sa.Boolean),
        sa.Column("hardFail", sa.Boolean),
        sa.Column("offline", sa.Boolean),
        sa.Column("blackedOut", sa.Boolean),
        sa.Column("storeArtifactsLocally", sa.Boolean),
        sa.Column("socketTimeoutMillis", sa.Integer),
        sa.Column("localAddress", sa.String),
        sa.Column("retrievalCachePeriodSecs", sa.Integer),
        sa.Column("assumedOfflinePeriodSecs", sa.Integer),
        sa.Column("missedRetrievalCachePeriodSecs", sa.Integer),
        sa.Column("metadataRetrievalTimeoutSecs", sa.Integer),
        sa.Column("unusedArtifactsCleanupPeriodHours", sa.Integer),
        sa.Column("shareConfiguration", sa.Boolean),
        sa.Column("synchronizeProperties", sa.Boolean),
        sa.Column(
            "propertySets", json_type
        ),  # This should be a relationship in a real model
        sa.Column("archiveBrowsingEnabled", sa.Boolean),
        sa.Column("listRemoteFolderItems", sa.Boolean),
        sa.Column("allowAnyHostAuth", sa.Boolean),
        sa.Column("enableCookieManagement", sa.Boolean),
        sa.Column("propagateQueryParams", sa.Boolean),
        sa.Column("blockMismatchingMimeTypes", sa.Boolean),
        sa.Column("mismatchingMimeTypesOverrideList", sa.String),
        sa.Column("bypassHeadRequests", sa.Boolean),
        sa.Column("disableUrlNormalization", sa.Boolean),
        sa.Column(
            "contentSynchronisation", json_type
        ),  # This should be a relationship in a real model
        sa.Column("sendContext", sa.Boolean),
        sa.Column("passThrough", sa.Boolean),
        sa.Column("curated", sa.Boolean),
        sa.Column("retrieveSha256FromServer", sa.Boolean),
        sa.Column("xrayDataTtl", sa.Integer),
        sa.Column("downloadRedirect", sa.Boolean),
        sa.Column("xrayIndex", sa.Boolean),
        sa.Column("rclass", sa.String),
        sa.Column("handleReleases", sa.Boolean),
        sa.Column("handleSnapshots", sa.Boolean),
        sa.Column("suppressPomConsistencyChecks", sa.Boolean),
        sa.Column("remoteRepoChecksumPolicyType", sa.String),
        sa.Column("fetchJarsEagerly", sa.Boolean),
        sa.Column("fetchSourcesEagerly", sa.Boolean),
        sa.Column("maxUniqueSnapshots", sa.Integer),
        sa.Column("rejectInvalidJars", sa.Boolean),
        sa.Column("vcsType", sa.String),
        sa.Column("composerRegistryUrl", sa.String),
        sa.Column("vcsGitProvider", sa.String),
        sa.Column("pyPIRegistryUrl", sa.String),
        sa.Column("pyPIRepositorySuffix", sa.String),
        sa.Column("externalDependenciesEnabled", sa.Boolean),
        sa.Column(
            "externalDependenciesPatterns", json_type
        ),  # This should be a relationship in a real model
        sa.Column("projectKey", sa.String),
        sa.Column("forceNugetAuthentication", sa.Boolean),
        sa.Column("enableNormalizedVersion", sa.Boolean),
        sa.Column("downloadContextPath", sa.String),
        sa.Column("feedContextPath", sa.String),
        sa.Column("v3FeedUrl", sa.String),
        sa.Column("symbolServerUrl", sa.String),
        sa.Column("dockerApiVersion", sa.String),
        sa.Column("blockPushingSchema1", sa.Boolean),
        sa.Column("dockerProjectId", sa.String),
        sa.Column("enableTokenAuthentication", sa.Boolean),
        sa.Column("forceConanAuthentication", sa.Boolean),
        sa.Column("terraformRegistryUrl", sa.String),
        sa.Column("terraformProvidersUrl", sa.String),
        sa.Column("ddebSupported", sa.Boolean),
        sa.Column("cargoAnonymousAccess", sa.Boolean),
        sa.Column("cargoInternalIndex", sa.Boolean),
        sa.Column("gitRegistryUrl", sa.String),
        sa.Column("remoteRepoLayoutRef", sa.String),
        sa.Column("podsCdnUrl", sa.String),
        sa.Column("podsSpecsRepoUrl", sa.String),
        sa.Column("podsForceModifyIndex", sa.Boolean),
        sa.Column("forceP2Authentication", sa.Boolean),
    )

    op.create_table(
        "virtual_item",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("packageType", sa.String),
        sa.Column("description", sa.String),
        sa.Column("notes", sa.String),
        sa.Column("includesPattern", sa.String),
        sa.Column("excludesPattern", sa.String),
        sa.Column("repoLayoutRef", sa.String),
        sa.Column("signedUrlTtl", sa.Integer),
        sa.Column(
            "environments", json_type
        ),  # This should be a relationship in a real model
        sa.Column(
            "repositories", json_type
        ),  # This should be a relationship in a real model
        sa.Column("hideUnauthorizedResources", sa.Boolean),
        sa.Column("artifactoryRequestsCanRetrieveRemoteArtifacts", sa.Boolean),
        sa.Column("externalDependenciesEnabled", sa.Boolean),
        sa.Column(
            "externalDependenciesPatterns", json_type
        ),  # This should be a relationship in a real model
        sa.Column("virtualRetrievalCachePeriodSecs", sa.Integer),
        sa.Column("rclass", sa.String),
        sa.Column("defaultDeploymentRepo", sa.String),
        sa.Column("keyPair", sa.String),
        sa.Column("pomRepositoryReferencesCleanupPolicy", sa.String),
        sa.Column("forceMavenAuthentication", sa.Boolean),
        sa.Column("projectKey", sa.String),
        sa.Column("forceNugetAuthentication", sa.Boolean),
        sa.Column("enableNormalizedVersion", sa.Boolean),
        sa.Column("dockerApiVersion", sa.String),
        sa.Column("resolveDockerTagsByTimestamp", sa.Boolean),
        sa.Column("cachingLocalForeignLayersEnabled", sa.Boolean),
        sa.Column("externalDependenciesRemoteRepo", sa.String),
        sa.Column("forceConanAuthentication", sa.Boolean),
        sa.Column("useNamespaces", sa.Boolean),
        sa.Column("ddebSupported", sa.Boolean),
        sa.Column("debianDefaultArchitectures", sa.String),
        sa.Column(
            "optionalIndexCompressionFormats", json_type
        ),  # This should be a relationship in a real model
        sa.Column("forceP2Authentication", sa.Boolean),
        sa.Column(
            "p2Urls", json_type
        ),  # This should be a relationship in a real model
    )

    op.create_table(
        "federated_item",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("packageType", sa.String),
        sa.Column("description", sa.String),
        sa.Column("notes", sa.String),
        sa.Column("includesPattern", sa.String),
        sa.Column("excludesPattern", sa.String),
        sa.Column("repoLayoutRef", sa.String),
        sa.Column("signedUrlTtl", sa.Integer),
        sa.Column("priorityResolution", sa.Boolean),
        sa.Column(
            "environments", json_type
        ),  # This should be a relationship in a real model
        sa.Column("checksumPolicyType", sa.String),
        sa.Column("handleReleases", sa.Boolean),
        sa.Column("handleSnapshots", sa.Boolean),
        sa.Column("maxUniqueSnapshots", sa.Integer),
        sa.Column("snapshotVersionBehavior", sa.String),
        sa.Column("suppressPomConsistencyChecks", sa.Boolean),
        sa.Column("blackedOut", sa.Boolean),
        sa.Column(
            "propertySets", json_type
        ),  # This should be a relationship in a real model
        sa.Column("archiveBrowsingEnabled", sa.Boolean),
        sa.Column(
            "members", json_type
        ),  # This should be a relationship in a real model
        sa.Column("disableProxy", sa.Boolean),
        sa.Column("downloadRedirect", sa.Boolean),
        sa.Column("cdnRedirect", sa.Boolean),
        sa.Column("xrayIndex", sa.Boolean),
        sa.Column("xrayDataTtl", sa.Integer),
        sa.Column("rclass", sa.String),
        sa.Column("debianTrivialLayout", sa.Boolean),
        sa.Column("ddebSupported", sa.Boolean),
        sa.Column(
            "optionalIndexCompressionFormats", json_type
        ),  # This should be a relationship in a real model
        sa.Column("projectKey", sa.String),
        sa.Column("forceNugetAuthentication", sa.Boolean),
        sa.Column("enableNormalizedVersion", sa.Boolean),
        sa.Column("dockerApiVersion", sa.String),
        sa.Column("blockPushingSchema1", sa.Boolean),
        sa.Column("maxUniqueTags", sa.Integer),
        sa.Column("dockerTagRetention", sa.Integer),
    )

    op.create_table(
        "release_bundle_item",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("packageType", sa.String),
        sa.Column("description", sa.String),
        sa.Column("notes", sa.String),
        sa.Column("includesPattern", sa.String),
        sa.Column("excludesPattern", sa.String),
        sa.Column("repoLayoutRef", sa.String, nullable=True),
        sa.Column("signedUrlTtl", sa.Integer),
        sa.Column("priorityResolution", sa.Boolean),
        sa.Column(
            "environments", json_type
        ),  # This should be a relationship in a real model
        sa.Column("blackedOut", sa.Boolean),
        sa.Column(
            "propertySets", json_type
        ),  # This should be a relationship in a real model
        sa.Column("archiveBrowsingEnabled", sa.Boolean),
        sa.Column("xrayDataTtl", sa.Integer),
        sa.Column("downloadRedirect", sa.Boolean),
        sa.Column("cdnRedirect", sa.Boolean),
        sa.Column("xrayIndex", sa.Boolean),
        sa.Column("rclass", sa.String),
    )

    op.create_table(
        "violations",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("description", sa.String, nullable=False),
        sa.Column("severity", sa.String, nullable=False),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("infected_components", json_type, nullable=False),
        sa.Column("created", sa.DateTime, nullable=False),
        sa.Column("watch_name", sa.String, nullable=False),
        sa.Column("issue_id", sa.String, nullable=False),
        sa.Column(
            "violation_details_url",
            sa.String,
            nullable=False,
        ),
        sa.Column("impacted_artifacts", json_type, nullable=False),
    )

    op.create_table(
        "violations_hwm",
        sa.Column(
            "created_hwm", sa.DateTime, nullable=False, primary_key=True
        ),
    )

    op.create_table(
        "watches",
        sa.Column("id", sa.String),
        sa.Column("name", sa.String, nullable=True, primary_key=True),
        sa.Column("active", sa.Boolean, nullable=True),
        sa.Column("project_key", sa.String, nullable=True),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("project_resources", json_type, nullable=True),
        sa.Column("assigned_policies", json_type, nullable=True),
        sa.Column("ticket_generation", json_type, nullable=True),
        sa.Column("watch_recipients", json_type, nullable=True),
        sa.Column("create_ticket_enabled", sa.Boolean, nullable=True),
        sa.Column("ticket_profile", sa.String, nullable=True),
    )


def downgrade() -> None:
    pass
