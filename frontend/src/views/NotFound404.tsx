import React, { FC } from 'react';
import { Container, Row, Col } from 'react-bootstrap';

export const NotFound404: FC = () => {
  return (
    <>
      <Container className="h-100">
        <Row className="h-50 justify-content-center align-items-center">
          <Col className="text-center">
            <h1>404: Resource Not Found !</h1>
            <p>The shortlink or page you are looking for doesn't exist.</p>
          </Col>
        </Row>
      </Container>
    </>
  );
};
