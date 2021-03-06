insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_assessment'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_assessment'),'assessment_name');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_assessment'),'assessment_weight');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_assessment'),'assessment_type');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_assessment'),'module_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_leafassessment'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_leafassessment'),'leaf_name');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_leafassessment'),'assessment_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_leafassessment'),'max_mark');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_leafassessment'),'published');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'leaf_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'mark');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'session_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'marker');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'student');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markallocation'),'timeStamp');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markermodule'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markermodule'),'marker_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markermodule'),'module_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markersessions'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markersessions'),'marker_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_markersessions'),'session_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_module'),'code');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'session_name');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'assessment_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'opened');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'closed');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_sessions'),'status');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_studentsessions'),'id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_studentsessions'),'sess_id_id');
insert into dbModels_audittablecolumn (auditTableId_id,columnName) values((select id from dbModels_audittable where tableName='dbModels_studentsessions'),'student_id');
