import React, { FC, useState } from 'react';
import { API_DOCS_URL } from '../config/settings';
import SwaggerUI from 'swagger-ui-react';
import 'swagger-ui-react/swagger-ui.css';
export const Documentation: FC = () => <SwaggerUI url={API_DOCS_URL} />;
