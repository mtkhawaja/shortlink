import React, { FC, useState } from 'react';
import { URLForm, ShortlinkModal, CopyToast } from '../components/';
import { Container, Row, Col } from 'react-bootstrap';

export const Home: FC = () => {
  const [shortlink, setShortlink] = useState('');
  const [originalURL, setOriginalURL] = useState('');
  const [showToast, setShowToast] = useState(false);

  return (
    <>
      <Container className="h-100 pt-5 mt-5">
        <Row className="pt-5 mt-5 justify-content-center align-items-center">
          <Col sm={12}>
            <URLForm
              setShortlink={setShortlink}
              setOriginalURL={setOriginalURL}
            />
          </Col>
          <Col className="pt-5">
            <ShortlinkModal
              originalURL={originalURL}
              shortlinkURL={shortlink}
              setShowToast={setShowToast}
            />
          </Col>
        </Row>
        <CopyToast showToast={showToast} setShowToast={setShowToast} />
      </Container>
    </>
  );
};
