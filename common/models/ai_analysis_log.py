from common.database import BaseModel, HasStandardSetting, db
from sqlalchemy import types

class AiAnalysisLog(HasStandardSetting, BaseModel):
	__tablename__ = 'ai_analysis_log'

	id	= db.Column(types.Integer, autoincrement=True, primary_key=True)
	image_path	= db.Column(types.VARCHAR(255), default= None)
	success	= db.Column(types.Boolean)
	message	= db.Column(types.VARCHAR(255), default= None)
	class_label	= db.Column(types.Integer, default= None)
	confidence	= db.Column(types.Numeric(5,4), default= None)
	request_timestamp	= db.Column(types.DateTime(6), default= None)
	response_timestamp	= db.Column(types.DateTime(6), default= None)
