import React, { FC } from 'react';
import { URLInputField } from '../components/URLInputField';
import { Container, Row, Col } from 'react-bootstrap';
export const Home: FC = () => {
  return (
    <>
      <Container className="h-100">
        <Row className="h-50 justify-content-center align-items-center">
          <Col>
            <URLInputField />
          </Col>
        </Row>
      </Container>
    </>
  );
};
