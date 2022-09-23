class XcalError(Exception):
    """Base class for exceptions in this module."""
    pass


class Success(XcalError):
    # SUCCESS
    pass


class EParameters(XcalError):
    # E_PARAMETERS
    pass


class EJobTypeUnknown(XcalError):
    # E_JOB_TYPE_UNKNOWN
    pass


class ESubprocessFail(XcalError):
    # E_SUBPROCESS_FAIL
    pass


class ECollectTarFailed(XcalError):
    # E_COLLECT_TAR_FAILED
    pass


class EUploadPreprocessTarFailed(XcalError):
    # E_UPLOAD_PREPROCESS_TAR_FAILED
    pass


class EReportResultFailed(XcalError):
    # E_REPORT_RESULT_FAILED
    pass


class EApiInvokeFail(XcalError):
    # E_API_INVOKE_FAIL
    pass


class EXcalbuildNotFound(XcalError):
    # E_XCALBUILD_NOT_FOUND
    pass


class ECmdReturnNonzero(XcalError):
    # E_CMD_RETURN_NONZERO
    pass


class EJobTypeNone(XcalError):
    # E_JOB_TYPE_NONE
    pass


class EJavaScanFail(XcalError):
    # E_JAVA_SCAN_FAIL
    pass


class EFileInfoPjNull(XcalError):
    # E_FILE_INFO_PJ_NULL
    pass


class EFileInfoGatherFail(XcalError):
    # E_FILE_INFO_GATHER_FAIL
    pass


class EPluginReturnNonzero(XcalError):
    # E_PLUGIN_RETURN_NONZERO
    pass


class EPluginExecErr(XcalError):
    # E_PLUGIN_EXEC_ERR
    pass


class EPrescanResultDirNonexist(XcalError):
    # E_PRESCAN_RESULT_DIR_NONEXIST
    pass


class ENoViableMiddleResult(XcalError):
    # E_NO_VIABLE_MIDDLE_RESULT
    pass


class ENotFoundFile(XcalError):
    # E_NOT_FOUND_FILE
    pass


class ECompressFail(XcalError):
    # E_COMPRESS_FAIL
    pass


class EExtractUnknownFilekind(XcalError):
    # E_EXTRACT_UNKNOWN_FILEKIND
    pass


class EConfigParmError(XcalError):
    # E_CONFIG_PARM_ERROR
    pass


class EConfigSetValueWrongkind(XcalError):
    # E_CONFIG_SET_VALUE_WRONGKIND
    pass


class EFileutilDirstack(XcalError):
    # E_FILEUTIL_DIRSTACK
    pass


class EFolderPermissionError(XcalError):
    # E_FOLDER_PERMISSION_ERROR
    pass


class EGitCloneFailed(XcalError):
    # E_GIT_CLONE_FAILED
    pass


class EFileinfoFolderNonexist(XcalError):
    # E_FILEINFO_FOLDER_NONEXIST
    pass


class EJavaPreprocessNoOutput(XcalError):
    # E_JAVA_PREPROCESS_NO_OUTPUT
    pass


class EJavaHomeNotvalid(XcalError):
    # E_JAVA_HOME_NOTVALID
    pass


class EJobConfigAppendFail(XcalError):
    # E_JOB_CONFIG_APPEND_FAIL
    pass


class ECheckCacheFileFailed(XcalError):
    # E_CHECK_CACHE_FILE_FAILED
    pass


class ECheckCacheNoneFileid(XcalError):
    # E_CHECK_CACHE_NONE_FILEID
    pass


class EFileInfoNoUploadresults(XcalError):
    # E_FILE_INFO_NO_UPLOADRESULTS
    pass


class EFileInfoNoFileid(XcalError):
    # E_FILE_INFO_NO_FILEID
    pass


class EFolderNotexist(XcalError):
    # E_FOLDER_NOTEXIST
    pass


class EVariableMustHaveValue(XcalError):
    # E_VARIABLE_MUST_HAVE_VALUE
    pass


class EScanServiceVersionMismatch(XcalError):
    # E_SCAN_SERVICE_VERSION_MISMATCH
    pass


class EFeUtilDirNotfound(XcalError):
    # E_FE_UTIL_DIR_NOTFOUND
    pass


class EFeUtilDirUnreadable(XcalError):
    # E_FE_UTIL_DIR_UNREADABLE
    pass


class EFeUtilLibNotfound(XcalError):
    # E_FE_UTIL_LIB_NOTFOUND
    pass


class EFeUtilLibUnreadable(XcalError):
    # E_FE_UTIL_LIB_UNREADABLE
    pass


class EFeUtilJarNotfound(XcalError):
    # E_FE_UTIL_JAR_NOTFOUND
    pass


class EFeUtilJarUnreadable(XcalError):
    # E_FE_UTIL_JAR_UNREADABLE
    pass


class EJdkJarNotfound(XcalError):
    # E_JDK_JAR_NOTFOUND
    pass


class EJdkJarUnreadable(XcalError):
    # E_JDK_JAR_UNREADABLE
    pass


class EJfeReturnNonzero(XcalError):
    # E_JFE_RETURN_NONZERO
    pass


class ERtObjNonExist(XcalError):
    # E_RT_OBJ_NON_EXIST
    pass


class ERtTarNotExist(XcalError):
    # E_RT_TAR_NOT_EXIST
    pass


class ECheckFileCachedNonJson(XcalError):
    # E_CHECK_FILE_CACHED_NON_JSON
    pass


class EScanConnResNotExist(XcalError):
    # E_SCAN_CONN_RES_NOT_EXIST
    pass


class EFeUtilConnNotfound(XcalError):
    # E_FE_UTIL_CONN_NOTFOUND
    pass


class EFeUtilConnUnreadable(XcalError):
    # E_FE_UTIL_CONN_UNREADABLE
    pass


class EScanConnRetNonzero(XcalError):
    # E_SCAN_CONN_RET_NONZERO
    pass


class EConnectorNotfound(XcalError):
    # E_CONNECTOR_NOTFOUND
    pass


class EConnectorUnreadable(XcalError):
    # E_CONNECTOR_UNREADABLE
    pass


class EPollTaskFailed(XcalError):
    # E_POLL_TASK_FAILED
    pass


class EInvalidJsonFormat(XcalError):
    # E_INVALID_JSON_FORMAT
    pass


class ECheckFileCachedNetFail(XcalError):
    # E_CHECK_FILE_CACHED_NET_FAIL
    pass


class ELoginFail(XcalError):
    # E_LOGIN_FAIL
    pass


class ELoginResponseNonJson(XcalError):
    # E_LOGIN_RESPONSE_NON_JSON
    pass


class ESaveFileCachedNonJson(XcalError):
    # E_SAVE_FILE_CACHED_NON_JSON
    pass


class ESaveFileCachedNetFail(XcalError):
    # E_SAVE_FILE_CACHED_NET_FAIL
    pass


class ESaveFileCacheServerFail(XcalError):
    # E_SAVE_FILE_CACHE_SERVER_FAIL
    pass


class ESaveFileIdNotFound(XcalError):
    # E_SAVE_FILE_ID_NOT_FOUND
    pass


class EJavaPrescanPluginNotViable(XcalError):
    # E_JAVA_PRESCAN_PLUGIN_NOT_VIABLE
    pass


class EJavaPreprocessResultDirNotExist(XcalError):
    # E_JAVA_PREPROCESS_RESULT_DIR_NOT_EXIST
    pass


class ECommonFolderNonexist(XcalError):
    # E_COMMON_FOLDER_NONEXIST
    pass


class ECommonFolderPermission(XcalError):
    # E_COMMON_FOLDER_PERMISSION
    pass


class ECommonTimeout(XcalError):
    # E_COMMON_TIMEOUT
    pass


class ECommonFileNotExist(XcalError):
    # E_COMMON_FILE_NOT_EXIST
    pass


class ECommonInvalidContent(XcalError):
    # E_COMMON_INVALID_CONTENT
    pass


class EAgentCheckTypeNotSupport(XcalError):
    # E_AGENT_CHECK_TYPE_NOT_SUPPORT
    pass


class ESysDependencyNotExist(XcalError):
    # E_SYS_DEPENDENCY_NOT_EXIST
    pass


class EPyDependencyNotExist(XcalError):
    # E_PY_DEPENDENCY_NOT_EXIST
    pass


class EPluginTypeNotSupport(XcalError):
    # E_PLUGIN_TYPE_NOT_SUPPORT
    pass


class EPluginInstallationFailed(XcalError):
    # E_PLUGIN_INSTALLATION_FAILED
    pass


class EComponentMissing(XcalError):
    # E_COMPONENT_MISSING
    pass


class EJavaHomeNotFound(XcalError):
    # E_JAVA_HOME_NOT_FOUND
    pass


class ENoSufficientMemory(XcalError):
    # E_NO_SUFFICIENT_MEMORY
    pass


class EBearInstallationFailed(XcalError):
    # E_BEAR_INSTALLATION_FAILED
    pass


class ENoAgentConnTimeout(XcalError):
    # E_NO_AGENT_CONN_TIMEOUT
    pass


class EScanTimeExceed(XcalError):
    # E_SCAN_TIME_EXCEED
    pass


class EScanUploadTimeout(XcalError):
    # E_SCAN_UPLOAD_TIMEOUT
    pass


class EQueueingExpired(XcalError):
    # E_QUEUEING_EXPIRED
    pass


class EScanServiceStageTimeout(XcalError):
    # E_SCAN_SERVICE_STAGE_TIMEOUT
    pass


class ESourceDirectoryNotExist(XcalError):
    # E_SOURCE_DIRECTORY_NOT_EXIST
    pass


class EBuildMainDirectoryNotExist(XcalError):
    # E_BUILD_MAIN_DIRECTORY_NOT_EXIST
    pass


class EAgentNameInvalid(XcalError):
    # E_AGENT_NAME_INVALID
    pass


class EJobQueueNameInvalid(XcalError):
    # E_JOB_QUEUE_NAME_INVALID
    pass


class ENoAgentToken(XcalError):
    # E_NO_AGENT_TOKEN
    pass


class EJavaParseUserEnvopt(XcalError):
    # E_JAVA_PARSE_USER_ENVOPT
    pass


class EUtilTarCompress(XcalError):
    # E_UTIL_TAR_COMPRESS
    pass


class EUtilUnknownArchiveType(XcalError):
    # E_UTIL_UNKNOWN_ARCHIVE_TYPE
    pass


class EUtilConfobjParam(XcalError):
    # E_UTIL_CONFOBJ_PARAM
    pass


class EUtilConfobjToken(XcalError):
    # E_UTIL_CONFOBJ_TOKEN
    pass


class EUtilConfobjUsercontent(XcalError):
    # E_UTIL_CONFOBJ_USERCONTENT
    pass


class EUtilConfobjScanid(XcalError):
    # E_UTIL_CONFOBJ_SCANID
    pass


class EUtilConfobjScanfile(XcalError):
    # E_UTIL_CONFOBJ_SCANFILE
    pass


class EUtilConfobjPreprocpath(XcalError):
    # E_UTIL_CONFOBJ_PREPROCPATH
    pass


class EUtilConfobjSet(XcalError):
    # E_UTIL_CONFOBJ_SET
    pass


class EUtilExpireNoneHooktype(XcalError):
    # E_UTIL_EXPIRE_NONE_HOOKTYPE
    pass


class EStageNotRecognize(XcalError):
    # E_STAGE_NOT_RECOGNIZE
    pass


class EUtilExpireUnknownListName(XcalError):
    # E_UTIL_EXPIRE_UNKNOWN_LIST_NAME
    pass


class EUtilExpireIgnoreDuration(XcalError):
    # E_UTIL_EXPIRE_IGNORE_DURATION
    pass


class EUtilZipCompress(XcalError):
    # E_UTIL_ZIP_COMPRESS
    pass


class EScanJobFailed(XcalError):
    # E_SCAN_JOB_FAILED
    pass


class ENoPipeline(XcalError):
    # E_NO_PIPELINE
    pass


class EPipelineOffset(XcalError):
    # E_PIPELINE_OFFSET
    pass


class ESrvJoblistenKafkaReceive(XcalError):
    # E_SRV_JOBLISTEN_KAFKA_RECEIVE
    pass


class EJobExpire(XcalError):
    # E_JOB_EXPIRE
    pass


class ESrvKafkaFailed(XcalError):
    # E_SRV_KAFKA_FAILED
    pass


class EApiAgentParamTarget(XcalError):
    # E_API_AGENT_PARAM_TARGET
    pass


class ESrvAgentInvokeKeyInConfig(XcalError):
    # E_SRV_AGENT_INVOKE_KEY_IN_CONFIG
    pass


class ESrvAgentInvokeGitlab(XcalError):
    # E_SRV_AGENT_INVOKE_GITLAB
    pass


class ESrvAgentSrcAddress(XcalError):
    # E_SRV_AGENT_SRC_ADDRESS
    pass


class ESrvAgentNoPreprocessLoc(XcalError):
    # E_SRV_AGENT_NO_PREPROCESS_LOC
    pass


class ESrvAgentSshFailed(XcalError):
    # E_SRV_AGENT_SSH_FAILED
    pass


class ESrvAgentSshParam(XcalError):
    # E_SRV_AGENT_SSH_PARAM
    pass


class ESrvFileScpSend(XcalError):
    # E_SRV_FILE_SCP_SEND
    pass


class ESrvFileScpGetFail(XcalError):
    # E_SRV_FILE_SCP_GET_FAIL
    pass


class ESrvGetpreprocNoPrescanResult(XcalError):
    # E_SRV_GETPREPROC_NO_PRESCAN_RESULT
    pass


class ESrvAgentUnknown(XcalError):
    # E_SRV_AGENT_UNKNOWN
    pass


class ESrvAgentCheckCache(XcalError):
    # E_SRV_AGENT_CHECK_CACHE
    pass


class ESrvXvsaUnknownExectuteType(XcalError):
    # E_SRV_XVSA_UNKNOWN_EXECTUTE_TYPE
    pass


class ESrvFlattenOversize(XcalError):
    # E_SRV_FLATTEN_OVERSIZE
    pass


class ESrvFlattenFidInvalid(XcalError):
    # E_SRV_FLATTEN_FID_INVALID
    pass


class ESrvFlattenPathFidInvalid(XcalError):
    # E_SRV_FLATTEN_PATH_FID_INVALID
    pass


class EUtilCacheNoneParam(XcalError):
    # E_UTIL_CACHE_NONE_PARAM
    pass


class EUtilCacheJsonInvalid(XcalError):
    # E_UTIL_CACHE_JSON_INVALID
    pass


class ESettingSetParmError(XcalError):
    # E_SETTING_SET_PARM_ERROR
    pass


class EDockerConatinerExitnzero(XcalError):
    # E_DOCKER_CONATINER_EXITNZERO
    pass


class EDockerNoimagefound(XcalError):
    # E_DOCKER_NOIMAGEFOUND
    pass


class EDockerApiError(XcalError):
    # E_DOCKER_API_ERROR
    pass


class ESrvXvsaExecuteFail(XcalError):
    # E_SRV_XVSA_EXECUTE_FAIL
    pass


class ESrvXvsaDockerFail(XcalError):
    # E_SRV_XVSA_DOCKER_FAIL
    pass


class ESrvUploadNoVFile(XcalError):
    # E_SRV_UPLOAD_NO_V_FILE
    pass


class ESrvUploadVNotReadable(XcalError):
    # E_SRV_UPLOAD_V_NOT_READABLE
    pass


class ESrvUploadFileinfoNexist(XcalError):
    # E_SRV_UPLOAD_FILEINFO_NEXIST
    pass


class ESrvUploadFileinfoNotReadable(XcalError):
    # E_SRV_UPLOAD_FILEINFO_NOT_READABLE
    pass


class ESrvUploadVFileOversize(XcalError):
    # E_SRV_UPLOAD_V_FILE_OVERSIZE
    pass


class ESrvUploadFileinfoOversize(XcalError):
    # E_SRV_UPLOAD_FILEINFO_OVERSIZE
    pass


class EConnectApiListSetting(XcalError):
    # E_CONNECT_API_LIST_SETTING
    pass


class EConnectApiUploadProgress(XcalError):
    # E_CONNECT_API_UPLOAD_PROGRESS
    pass


class EGetCurrentUserInfoFailed(XcalError):
    # E_GET_CURRENT_USER_INFO_FAILED
    pass


class ECreateProjectFailed(XcalError):
    # E_CREATE_PROJECT_FAILED
    pass


class EGetProjectConfigFailed(XcalError):
    # E_GET_PROJECT_CONFIG_FAILED
    pass


class EAddScanTaskFailed(XcalError):
    # E_ADD_SCAN_TASK_FAILED
    pass


class ECallScanServiceFailed(XcalError):
    # E_CALL_SCAN_SERVICE_FAILED
    pass


class EKeyNotFound(XcalError):
    # E_KEY_NOT_FOUND
    pass


class ENoScanResult(XcalError):
    # E_NO_SCAN_RESULT
    pass


class EApiValidationConstraintsNotblank(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_NOTBLANK
    pass


class EApiValidationConstraintsNotnull(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_NOTNULL
    pass


class EApiValidationConstraintsPattern(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_PATTERN
    pass


class EApiValidationConstraintsEmail(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_EMAIL
    pass


class EApiValidationConstraintsSize(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_SIZE
    pass


class EApiValidationConstraintsPort(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_PORT
    pass


class EApiValidationConstraintsMin(XcalError):
    # E_API_VALIDATION_CONSTRAINTS_MIN
    pass


class EApiCommonCommonInternalError(XcalError):
    # E_API_COMMON_COMMON_INTERNAL_ERROR
    pass


class EApiCommonCommonNotImplement(XcalError):
    # E_API_COMMON_COMMON_NOT_IMPLEMENT
    pass


class EApiCommonCommonInvalidConfig(XcalError):
    # E_API_COMMON_COMMON_INVALID_CONFIG
    pass


class EApiCommonCommonInvalidStatus(XcalError):
    # E_API_COMMON_COMMON_INVALID_STATUS
    pass


class EApiCommonDtoConvertParameterNotExist(XcalError):
    # E_API_COMMON_DTO_CONVERT_PARAMETER_NOT_EXIST
    pass


class EApiCommonDtoInvalidContent(XcalError):
    # E_API_COMMON_DTO_INVALID_CONTENT
    pass


class EApiCommonMissingFile(XcalError):
    # E_API_COMMON_MISSING_FILE
    pass


class EApiEmailCommonSendmail(XcalError):
    # E_API_EMAIL_COMMON_SENDMAIL
    pass


class EApiEmailCommonUnassignedIssue(XcalError):
    # E_API_EMAIL_COMMON_UNASSIGNED_ISSUE
    pass


class EApiEmailPrepareFailed(XcalError):
    # E_API_EMAIL_PREPARE_FAILED
    pass


class EApiFileAddAlreadyExist(XcalError):
    # E_API_FILE_ADD_ALREADY_EXIST
    pass


class EApiFileCheckintegrityFailed(XcalError):
    # E_API_FILE_CHECKINTEGRITY_FAILED
    pass


class EApiFileChecksumNotParsable(XcalError):
    # E_API_FILE_CHECKSUM_NOT_PARSABLE
    pass


class EApiFileCommonFileinformationAlreadyExist(XcalError):
    # E_API_FILE_COMMON_FILEINFORMATION_ALREADY_EXIST
    pass


class EApiFileCommonFileinformationNotFound(XcalError):
    # E_API_FILE_COMMON_FILEINFORMATION_NOT_FOUND
    pass


class EApiFileCommonInvalidFormat(XcalError):
    # E_API_FILE_COMMON_INVALID_FORMAT
    pass


class EApiFileCommonInvalidType(XcalError):
    # E_API_FILE_COMMON_INVALID_TYPE
    pass


class EApiFileCommonInvalidValue(XcalError):
    # E_API_FILE_COMMON_INVALID_VALUE
    pass


class EApiFileCommonInvalidStorageType(XcalError):
    # E_API_FILE_COMMON_INVALID_STORAGE_TYPE
    pass


class EApiFileCommonNotAvailable(XcalError):
    # E_API_FILE_COMMON_NOT_AVAILABLE
    pass


class EApiFileCommonNotFound(XcalError):
    # E_API_FILE_COMMON_NOT_FOUND
    pass


class EApiFileCommonObtainFailed(XcalError):
    # E_API_FILE_COMMON_OBTAIN_FAILED
    pass


class EApiFileCommonCreateTempFileFailed(XcalError):
    # E_API_FILE_COMMON_CREATE_TEMP_FILE_FAILED
    pass


class EApiFileCompressfileCopycodeFailed(XcalError):
    # E_API_FILE_COMPRESSFILE_COPYCODE_FAILED
    pass


class EApiFileCompressfileDecompressFailed(XcalError):
    # E_API_FILE_COMPRESSFILE_DECOMPRESS_FAILED
    pass


class EApiFileCompressfileDeleteExistingFailed(XcalError):
    # E_API_FILE_COMPRESSFILE_DELETE_EXISTING_FAILED
    pass


class EApiFileCompressfileFailed(XcalError):
    # E_API_FILE_COMPRESSFILE_FAILED
    pass


class EApiFileCompressfileFileNotGenerated(XcalError):
    # E_API_FILE_COMPRESSFILE_FILE_NOT_GENERATED
    pass


class EApiFileCompressfileFileOrDirectoryNotFound(XcalError):
    # E_API_FILE_COMPRESSFILE_FILE_OR_DIRECTORY_NOT_FOUND
    pass


class EApiFileGetfilestorageFailed(XcalError):
    # E_API_FILE_GETFILESTORAGE_FAILED
    pass


class EApiFileUploadFileFailed(XcalError):
    # E_API_FILE_UPLOAD_FILE_FAILED
    pass


class EApiFileImportFileFailed(XcalError):
    # E_API_FILE_IMPORT_FILE_FAILED
    pass


class EApiFileImportfileinfoRootNotFound(XcalError):
    # E_API_FILE_IMPORTFILEINFO_ROOT_NOT_FOUND
    pass


class EApiFileImportfileinfoParentNotFound(XcalError):
    # E_API_FILE_IMPORTFILEINFO_PARENT_NOT_FOUND
    pass


class EApiFilestorageAddAlreadyExist(XcalError):
    # E_API_FILESTORAGE_ADD_ALREADY_EXIST
    pass


class EApiFilestorageCommonNotFound(XcalError):
    # E_API_FILESTORAGE_COMMON_NOT_FOUND
    pass


class EApiGitCommonCloneFailed(XcalError):
    # E_API_GIT_COMMON_CLONE_FAILED
    pass


class EApiGitCommonCommitNotFound(XcalError):
    # E_API_GIT_COMMON_COMMIT_NOT_FOUND
    pass


class EApiGitCommonGitlaberror(XcalError):
    # E_API_GIT_COMMON_GITLABERROR
    pass


class EApiGitCommonLastCommitidNotFound(XcalError):
    # E_API_GIT_COMMON_LAST_COMMITID_NOT_FOUND
    pass


class EApiGitCommonProjectidNotBlank(XcalError):
    # E_API_GIT_COMMON_PROJECTID_NOT_BLANK
    pass


class EApiGitCommonProjectidorpathNotBlank(XcalError):
    # E_API_GIT_COMMON_PROJECTIDORPATH_NOT_BLANK
    pass


class EApiGitGetrawfileFailed(XcalError):
    # E_API_GIT_GETRAWFILE_FAILED
    pass


class EApiGitGetrepoFailed(XcalError):
    # E_API_GIT_GETREPO_FAILED
    pass


class EApiGitGithubprojecturlNotBlank(XcalError):
    # E_API_GIT_GITHUBPROJECTURL_NOT_BLANK
    pass


class EApiIssueCommonInvalidSeverity(XcalError):
    # E_API_ISSUE_COMMON_INVALID_SEVERITY
    pass


class EApiIssueCommonNotFound(XcalError):
    # E_API_ISSUE_COMMON_NOT_FOUND
    pass


class EApiIssueUpdateissueInvalidAction(XcalError):
    # E_API_ISSUE_UPDATEISSUE_INVALID_ACTION
    pass


class EApiIssueImportissueInvalidFile(XcalError):
    # E_API_ISSUE_IMPORTISSUE_INVALID_FILE
    pass


class EApiLicenseCommonExpired(XcalError):
    # E_API_LICENSE_COMMON_EXPIRED
    pass


class EApiLicenseCommonInvalidLicense(XcalError):
    # E_API_LICENSE_COMMON_INVALID_LICENSE
    pass


class EApiLicenseCommonNotFound(XcalError):
    # E_API_LICENSE_COMMON_NOT_FOUND
    pass


class EApiLicenseUpdatePublicKeyNotFound(XcalError):
    # E_API_LICENSE_UPDATE_PUBLIC_KEY_NOT_FOUND
    pass


class EApiLicenseUpdateEncryptAesKeyNotFound(XcalError):
    # E_API_LICENSE_UPDATE_ENCRYPT_AES_KEY_NOT_FOUND
    pass


class EApiProjectCommonNotFound(XcalError):
    # E_API_PROJECT_COMMON_NOT_FOUND
    pass


class EApiProjectCreateAlreadyExist(XcalError):
    # E_API_PROJECT_CREATE_ALREADY_EXIST
    pass


class EApiProjectUpdateInconsistent(XcalError):
    # E_API_PROJECT_UPDATE_INCONSISTENT
    pass


class EApiProjectconfigCanNotUpdateInScanning(XcalError):
    # E_API_PROJECTCONFIG_CAN_NOT_UPDATE_IN_SCANNING
    pass


class EApiProjectconfigCommonNotFound(XcalError):
    # E_API_PROJECTCONFIG_COMMON_NOT_FOUND
    pass


class EApiProjectconfigCreateAlreadyExist(XcalError):
    # E_API_PROJECTCONFIG_CREATE_ALREADY_EXIST
    pass


class EApiProjectconfigNotExist(XcalError):
    # E_API_PROJECTCONFIG_NOT_EXIST
    pass


class EApiPerformanceQueryDataFailed(XcalError):
    # E_API_PERFORMANCE_QUERY_DATA_FAILED
    pass


class EApiPerformanceCopyLogFileFailed(XcalError):
    # E_API_PERFORMANCE_COPY_LOG_FILE_FAILED
    pass


class EApiReportCommonCompileReportError(XcalError):
    # E_API_REPORT_COMMON_COMPILE_REPORT_ERROR
    pass


class EApiReportCommonGenerateReportError(XcalError):
    # E_API_REPORT_COMMON_GENERATE_REPORT_ERROR
    pass


class EApiRuleCommonAlreadyExist(XcalError):
    # E_API_RULE_COMMON_ALREADY_EXIST
    pass


class EApiRuleCommonCategoryNull(XcalError):
    # E_API_RULE_COMMON_CATEGORY_NULL
    pass


class EApiRuleCommonCodeNull(XcalError):
    # E_API_RULE_COMMON_CODE_NULL
    pass


class EApiRuleCommonNameNull(XcalError):
    # E_API_RULE_COMMON_NAME_NULL
    pass


class EApiRuleCommonNotFound(XcalError):
    # E_API_RULE_COMMON_NOT_FOUND
    pass


class EApiRuleCommonRulesetNotFound(XcalError):
    # E_API_RULE_COMMON_RULESET_NOT_FOUND
    pass


class EApiRuleInvalidScanEngine(XcalError):
    # E_API_RULE_INVALID_SCAN_ENGINE
    pass


class EApiScantaskAddscanInvalidOperation(XcalError):
    # E_API_SCANTASK_ADDSCAN_INVALID_OPERATION
    pass


class EApiScantaskCallscanCreatebodyFailed(XcalError):
    # E_API_SCANTASK_CALLSCAN_CREATEBODY_FAILED
    pass


class EApiScantaskCallscanExecuteFailed(XcalError):
    # E_API_SCANTASK_CALLSCAN_EXECUTE_FAILED
    pass


class EApiScantaskCanNotCompareDiffProject(XcalError):
    # E_API_SCANTASK_CAN_NOT_COMPARE_DIFF_PROJECT
    pass


class EApiScantaskCommonNotFound(XcalError):
    # E_API_SCANTASK_COMMON_NOT_FOUND
    pass


class EApiScantaskSummaryDataInconsistent(XcalError):
    # E_API_SCANTASK_SUMMARY_DATA_INCONSISTENT
    pass


class EApiScantaskConstructscanparamInvalidPreprocesspath(XcalError):
    # E_API_SCANTASK_CONSTRUCTSCANPARAM_INVALID_PREPROCESSPATH
    pass


class EApiScantaskConstructscanparamInvalidScanfilepath(XcalError):
    # E_API_SCANTASK_CONSTRUCTSCANPARAM_INVALID_SCANFILEPATH
    pass


class EApiScantaskConstructscanparamInvalidSourcestoragename(XcalError):
    # E_API_SCANTASK_CONSTRUCTSCANPARAM_INVALID_SOURCESTORAGENAME
    pass


class EApiScantaskConstructscanparamInvalidToken(XcalError):
    # E_API_SCANTASK_CONSTRUCTSCANPARAM_INVALID_TOKEN
    pass


class EApiScantaskPrepareforscanOnlySupportUpload(XcalError):
    # E_API_SCANTASK_PREPAREFORSCAN_ONLY_SUPPORT_UPLOAD
    pass


class EApiScantaskPrepareforscanInvalidFilestorageType(XcalError):
    # E_API_SCANTASK_PREPAREFORSCAN_INVALID_FILESTORAGE_TYPE
    pass


class EApiScantaskUpdateScanconfigFailed(XcalError):
    # E_API_SCANTASK_UPDATE_SCANCONFIG_FAILED
    pass


class EApiScantaskUpdateInconsistent(XcalError):
    # E_API_SCANTASK_UPDATE_INCONSISTENT
    pass


class EApiScantaskstatusCommonInvalidStatus(XcalError):
    # E_API_SCANTASKSTATUS_COMMON_INVALID_STATUS
    pass


class EApiScantaskstatusCommonInvalidStage(XcalError):
    # E_API_SCANTASKSTATUS_COMMON_INVALID_STAGE
    pass


class EApiScantaskstatusCommonNotFound(XcalError):
    # E_API_SCANTASKSTATUS_COMMON_NOT_FOUND
    pass


class EApiSettingAddAlreadyExist(XcalError):
    # E_API_SETTING_ADD_ALREADY_EXIST
    pass


class EApiSettingCommonNotFound(XcalError):
    # E_API_SETTING_COMMON_NOT_FOUND
    pass


class EApiSystemPingNotAvailable(XcalError):
    # E_API_SYSTEM_PING_NOT_AVAILABLE
    pass


class EApiUserAuthUsernamePasswordNotCorrect(XcalError):
    # E_API_USER_AUTH_USERNAME_PASSWORD_NOT_CORRECT
    pass


class EApiUserCommonInsufficientPrivilege(XcalError):
    # E_API_USER_COMMON_INSUFFICIENT_PRIVILEGE
    pass


class EApiUserCommonLocked(XcalError):
    # E_API_USER_COMMON_LOCKED
    pass


class EApiUserCommonNotFound(XcalError):
    # E_API_USER_COMMON_NOT_FOUND
    pass


class EApiUserCommonSuspended(XcalError):
    # E_API_USER_COMMON_SUSPENDED
    pass


class EApiUserCreateusersExceedlicensenumber(XcalError):
    # E_API_USER_CREATEUSERS_EXCEEDLICENSENUMBER
    pass


class EApiUserUpdatepasswordIncorrectPassword(XcalError):
    # E_API_USER_UPDATEPASSWORD_INCORRECT_PASSWORD
    pass


class EApiUserValidateusersEmailexist(XcalError):
    # E_API_USER_VALIDATEUSERS_EMAILEXIST
    pass


class EApiUserValidateusersUsernameexist(XcalError):
    # E_API_USER_VALIDATEUSERS_USERNAMEEXIST
    pass


class EApiUserValidateusersRowerror(XcalError):
    # E_API_USER_VALIDATEUSERS_ROWERROR
    pass


class EApiUserValidateusersValidationfailed(XcalError):
    # E_API_USER_VALIDATEUSERS_VALIDATIONFAILED
    pass


class EApiUsergroupAddusergroupsAlreadyexist(XcalError):
    # E_API_USERGROUP_ADDUSERGROUPS_ALREADYEXIST
    pass


class EApiUsergroupCommonCanNotDelete(XcalError):
    # E_API_USERGROUP_COMMON_CAN_NOT_DELETE
    pass


class EApiUsergroupCommonNotfound(XcalError):
    # E_API_USERGROUP_COMMON_NOTFOUND
    pass


class EApiScantaskTerminatedByUser(XcalError):
    # E_API_SCANTASK_TERMINATED_BY_USER
    pass


class EApiFileCommonGetPathFailed(XcalError):
    # E_API_FILE_COMMON_GET_PATH_FAILED
    pass


class EApiUserUpdateValidateFail(XcalError):
    # E_API_USER_UPDATE_VALIDATE_FAIL
    pass


class EApiProjectUpdateValidateFail(XcalError):
    # E_API_PROJECT_UPDATE_VALIDATE_FAIL
    pass


class EApiUserValidatePasswordValidateFail(XcalError):
    # E_API_USER_VALIDATE_PASSWORD_VALIDATE_FAIL
    pass


class EApiUsergroupCreateValidateFail(XcalError):
    # E_API_USERGROUP_CREATE_VALIDATE_FAIL
    pass


class EApiUserLoginValidateFail(XcalError):
    # E_API_USER_LOGIN_VALIDATE_FAIL
    pass


class EApiProjectCreateValidateFail(XcalError):
    # E_API_PROJECT_CREATE_VALIDATE_FAIL
    pass


class EApiProjectconfigCreateValidateFail(XcalError):
    # E_API_PROJECTCONFIG_CREATE_VALIDATE_FAIL
    pass


class EApiPresetCreateValidateFail(XcalError):
    # E_API_PRESET_CREATE_VALIDATE_FAIL
    pass


class EApiPresetUpdateValidateFail(XcalError):
    # E_API_PRESET_UPDATE_VALIDATE_FAIL
    pass


class EApiScantaskstatusUpdateValidateFail(XcalError):
    # E_API_SCANTASKSTATUS_UPDATE_VALIDATE_FAIL
    pass


class EApiPresetCreateSettingValidateFail(XcalError):
    # E_API_PRESET_CREATE_SETTING_VALIDATE_FAIL
    pass


class EApiPresetUpdateSettingValidateFail(XcalError):
    # E_API_PRESET_UPDATE_SETTING_VALIDATE_FAIL
    pass


class EApiEmailconfigUpdateSettingValidateFail(XcalError):
    # E_API_EMAILCONFIG_UPDATE_SETTING_VALIDATE_FAIL
    pass


class EApiContactusValidateFail(XcalError):
    # E_API_CONTACTUS_VALIDATE_FAIL
    pass


class EAgentIsBusy(XcalError):
    # E_AGENT_IS_BUSY
    pass


class ECommonUnknownError(XcalError):
    # E_COMMON_UNKNOWN_ERROR
    pass


class ENoActiveAgentForThisJob(XcalError):
    # E_NO_ACTIVE_AGENT_FOR_THIS_JOB
    pass


class ECommonInvalidValue(XcalError):
    # E_COMMON_INVALID_VALUE
    pass


class ESrvUploadFileinfoFailed(XcalError):
    # E_SRV_UPLOAD_FILEINFO_FAILED
    pass


class EImportResultAllFailed(XcalError):
    # E_IMPORT_RESULT_ALL_FAILED
    pass


class ESrvScanCancelled(XcalError):
    # E_SRV_SCAN_CANCELLED
    pass


class ESrvScanUnknownError(XcalError):
    # E_SRV_SCAN_UNKNOWN_ERROR
    pass


class ESpringBootSecuritySessionInvalid(XcalError):
    # E_SPRING_BOOT_SECURITY_SESSION_INVALID
    pass


class IScanProgress(XcalError):
    # I_SCAN_PROGRESS
    pass


class EScanLibIncompatible(XcalError):
    # E_SCAN_LIB_INCOMPATIBLE
    pass


class EApiFileCommonSourceCodeNotUpload(XcalError):
    # E_API_FILE_COMMON_SOURCE_CODE_NOT_UPLOAD
    pass


class ENetworkRequestTimeout(XcalError):
    # E_NETWORK_REQUEST_TIMEOUT
    pass


class EApiGitCommonGithuberror(XcalError):
    # E_API_GIT_COMMON_GITHUBERROR
    pass


class EGitDiffFailed(XcalError):
    # E_GIT_DIFF_FAILED
    pass


class EGitFetchCheckoutFailed(XcalError):
    # E_GIT_FETCH_CHECKOUT_FAILED
    pass


class EApiScantaskAddscanEmptyProjectUuid(XcalError):
    # E_API_SCANTASK_ADDSCAN_EMPTY_PROJECT_UUID
    pass


class EApiFileCommonArchiveHaveMoreThanOneFile(XcalError):
    # E_API_FILE_COMMON_ARCHIVE_HAVE_MORE_THAN_ONE_FILE
    pass


class EApiIssueImportissuediffInvalidFile(XcalError):
    # E_API_ISSUE_IMPORTISSUEDIFF_INVALID_FILE
    pass


class EApiGitProjecturlNotBlank(XcalError):
    # E_API_GIT_PROJECTURL_NOT_BLANK
    pass


class EGuiAddScanTaskFailed(XcalError):
    # E_GUI_ADD_SCAN_TASK_FAILED
    pass


class EGuiUploadFileFailed(XcalError):
    # E_GUI_UPLOAD_FILE_FAILED
    pass


class EGuiCreateProjectFailed(XcalError):
    # E_GUI_CREATE_PROJECT_FAILED
    pass


class EGuiStartScanFailed(XcalError):
    # E_GUI_START_SCAN_FAILED
    pass


class EGuiUnknownError(XcalError):
    # E_GUI_UNKNOWN_ERROR
    pass


class EGuiScanServerNoResponse(XcalError):
    # E_GUI_SCAN_SERVER_NO_RESPONSE
    pass


class EGuiInternalError(XcalError):
    # E_GUI_INTERNAL_ERROR
    pass


class EGuiLoginFailed(XcalError):
    # E_GUI_LOGIN_FAILED
    pass


class EApiFileCalculateHashFailed(XcalError):
    # E_API_FILE_CALCULATE_HASH_FAILED
    pass


class EApiGitCommonGiturlMismatch(XcalError):
    # E_API_GIT_COMMON_GITURL_MISMATCH
    pass


class EMavenSettingNotFound(XcalError):
    # E_MAVEN_SETTING_NOT_FOUND
    pass


class EBackupMavenLibraryFailed(XcalError):
    # E_BACKUP_MAVEN_LIBRARY_FAILED
    pass


class EFileSystemUrlErr(XcalError):
    # E_FILE_SYSTEM_URL_ERR
    pass


class EFileSystemKeyError(XcalError):
    # E_FILE_SYSTEM_KEY_ERROR
    pass


class EFileSystemFileError(XcalError):
    # E_FILE_SYSTEM_FILE_ERROR
    pass


class ENotCreateFolderInFileSystem(XcalError):
    # E_NOT_CREATE_FOLDER_IN_FILE_SYSTEM
    pass


class EGetTokenFailed(XcalError):
    # E_GET_TOKEN_FAILED
    pass


class MustProvidProjId(XcalError):
    # MUST_PROVID_PROJ_ID
    pass


class MustProvidProjInfo(XcalError):
    # MUST_PROVID_PROJ_INFO
    pass


class RunConfNotFound(XcalError):
    # RUN_CONF_NOT_FOUND
    pass


class RunConfError(XcalError):
    # RUN_CONF_ERROR
    pass


class UserConfNotFound(XcalError):
    # USER_CONF_NOT_FOUND
    pass


class EResourceNotFound(XcalError):
    # E_RESOURCE_NOT_FOUND
    pass


class EFsmInvalid(XcalError):
    # E_FSM_INVALID
    pass


class EMangleNameNotFound(XcalError):
    # E_MANGLE_NAME_NOT_FOUND
    pass


class EIncorrectApiCall(XcalError):
    # E_INCORRECT_API_CALL
    pass


class EApiNotExist(XcalError):
    # E_API_NOT_EXIST
    pass


class EInvalidFunctionFormat(XcalError):
    # E_INVALID_FUNCTION_FORMAT
    pass


class ELanguageNotSupported(XcalError):
    # E_LANGUAGE_NOT_SUPPORTED
    pass


class EMangleReferenceNotFound(XcalError):
    # E_MANGLE_REFERENCE_NOT_FOUND
    pass


class EXvsaCompileError(XcalError):
    # E_XVSA_COMPILE_ERROR
    pass


class EInfoFieldMissing(XcalError):
    # E_INFO_FIELD_MISSING
    pass


class EApiProjConfigAttrCmdNotFound(XcalError):
    # E_API_PROJ_CONFIG_ATTR_CMD_NOT_FOUND
    pass


class EWebApiAuthFailed(XcalError):
    # E_WEB_API_AUTH_FAILED
    pass


class EWebApiServiceError(XcalError):
    # E_WEB_API_SERVICE_ERROR
    pass


class EAgentDepInternalError(XcalError):
    # E_AGENT_DEP_INTERNAL_ERROR
    pass


class ESrvGitDiffNotExist(XcalError):
    # E_SRV_GIT_DIFF_NOT_EXIST
    pass


class ESrvBaselineVtxtNotExists(XcalError):
    # E_SRV_BASELINE_VTXT_NOT_EXISTS
    pass


class ESrvVtxtreaderNotExists(XcalError):
    # E_SRV_VTXTREADER_NOT_EXISTS
    pass


class ESrvVtxtreaderExecTimeout(XcalError):
    # E_SRV_VTXTREADER_EXEC_TIMEOUT
    pass


class ESrvVtxtreaderExecExecFailed(XcalError):
    # E_SRV_VTXTREADER_EXEC_EXEC_FAILED
    pass


class ESrvVtxtdiffNotExist(XcalError):
    # E_SRV_VTXTDIFF_NOT_EXIST
    pass


class ESrvVtxtdiffExecTimeOut(XcalError):
    # E_SRV_VTXTDIFF_EXEC_TIME_OUT
    pass


class ESrvVtxtdiffExecFailed(XcalError):
    # E_SRV_VTXTDIFF_EXEC_FAILED
    pass


class ESrvCurrentVtxtNotExist(XcalError):
    # E_SRV_CURRENT_VTXT_NOT_EXIST
    pass


class ESrvV2CsfNotExist(XcalError):
    # E_SRV_V2CSF_NOT_EXIST
    pass


class ESrvV2CsfTimeout(XcalError):
    # E_SRV_V2CSF_TIMEOUT
    pass


class ESrvV2CsfFailed(XcalError):
    # E_SRV_V2CSF_FAILED
    pass


class EWebApiServiceNoResponseError(XcalError):
    # E_WEB_API_SERVICE_NO_RESPONSE_ERROR
    pass


class ECsvInvalidInputFile(XcalError):
    # E_CSV_INVALID_INPUT_FILE
    pass


class ECsvOutOfMemory(XcalError):
    # E_CSV_OUT_OF_MEMORY
    pass


class ECsvInvalidOutputFile(XcalError):
    # E_CSV_INVALID_OUTPUT_FILE
    pass


class ECsvSize(XcalError):
    # E_CSV_SIZE
    pass


class EScanModeNotSupported(XcalError):
    # E_SCAN_MODE_NOT_SUPPORTED
    pass


class EAuthFailedUsernamePsw(XcalError):
    # E_AUTH_FAILED_USERNAME_PSW
    pass


class EAuthNoUsernamePsw(XcalError):
    # E_AUTH_NO_USERNAME_PSW
    pass


class EAuthFailed(XcalError):
    # E_AUTH_FAILED
    pass


class ELoginFailed(XcalError):
    # E_LOGIN_FAILED
    pass


class EClientArgValidateFailed(XcalError):
    # E_CLIENT_ARG_VALIDATE_FAILED
    pass


class EClientTimeoutMet(XcalError):
    # E_CLIENT_TIMEOUT_MET
    pass


class EClientSourceCodePathNotFound(XcalError):
    # E_CLIENT_SOURCE_CODE_PATH_NOT_FOUND
    pass


class EClientConfigNotFound(XcalError):
    # E_CLIENT_CONFIG_NOT_FOUND
    pass


class EClientConfigMalformed(XcalError):
    # E_CLIENT_CONFIG_MALFORMED
    pass


class EClientMissingScanConfig(XcalError):
    # E_CLIENT_MISSING_SCAN_CONFIG
    pass


class EClientWrongScanConfigPath(XcalError):
    # E_CLIENT_WRONG_SCAN_CONFIG_PATH
    pass


class EClientProjectPathNotFound(XcalError):
    # E_CLIENT_PROJECT_PATH_NOT_FOUND
    pass


class EClientNoScanRecordFound(XcalError):
    # E_CLIENT_NO_SCAN_RECORD_FOUND
    pass


class EClientCannotAccessWorkFolder(XcalError):
    # E_CLIENT_CANNOT_ACCESS_WORK_FOLDER
    pass


class EClientTaskException(XcalError):
    # E_CLIENT_TASK_EXCEPTION
    pass


class EClientWriteScanConfFailed(XcalError):
    # E_CLIENT_WRITE_SCAN_CONF_FAILED
    pass


class EClientNoScanConfFound(XcalError):
    # E_CLIENT_NO_SCAN_CONF_FOUND
    pass


class EClientProjectNameValidationFailed(XcalError):
    # E_CLIENT_PROJECT_NAME_VALIDATION_FAILED
    pass


class EClientFailedToCreateProject(XcalError):
    # E_CLIENT_FAILED_TO_CREATE_PROJECT
    pass


class EScmError(XcalError):
    # E_SCM_ERROR
    pass


class EClientProjectIdValidationFailed(XcalError):
    # E_CLIENT_PROJECT_ID_VALIDATION_FAILED
    pass


class EBuildFailedWithIFileGenerated(XcalError):
    # E_BUILD_FAILED_WITH_I_FILE_GENERATED
    pass


class EBuildSuccessNoIFileGenerated(XcalError):
    # E_BUILD_SUCCESS_NO_I_FILE_GENERATED
    pass


class EBuildFailedNoIFileGenerated(XcalError):
    # E_BUILD_FAILED_NO_I_FILE_GENERATED
    pass


class ENoIFileGenerated(XcalError):
    # E_NO_I_FILE_GENERATED
    pass


class EXcalbuildFail(XcalError):
    # E_XCALBUILD_FAIL
    pass


class EScmNoCommitBaselineId(XcalError):
    # E_SCM_NO_COMMIT_BASELINE_ID
    pass


class EUploadFileFailed(XcalError):
    # E_UPLOAD_FILE_FAILED
    pass


class EAccessFileServiceFailed(XcalError):
    # E_ACCESS_FILE_SERVICE_FAILED
    pass


class EDsrStateMissingRepoAction(XcalError):
    # E_DSR_STATE_MISSING_REPO_ACTION
    pass


class ENotSupportedRepoAction(XcalError):
    # E_NOT_SUPPORTED_REPO_ACTION
    pass


class ERepoActionValidationFailed(XcalError):
    # E_REPO_ACTION_VALIDATION_FAILED
    pass


class ERepoActionCiNotAllowToModify(XcalError):
    # E_REPO_ACTION_CI_NOT_ALLOW_TO_MODIFY
    pass


class EClientScanModeNotAllowedToModify(XcalError):
    # E_CLIENT_SCAN_MODE_NOT_ALLOWED_TO_MODIFY
    pass


class EPrepareBucketFailed(XcalError):
    # E_PREPARE_BUCKET_FAILED
    pass


class EGetProjectFromServerFailed(XcalError):
    # E_GET_PROJECT_FROM_SERVER_FAILED
    pass


class ERepoActionCdNotAllowToModify(XcalError):
    # E_REPO_ACTION_CD_NOT_ALLOW_TO_MODIFY
    pass


class EDuplicateProjectName(XcalError):
    # E_DUPLICATE_PROJECT_NAME
    pass


