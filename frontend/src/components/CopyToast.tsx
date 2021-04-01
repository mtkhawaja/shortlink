import React from 'react';
import Toast from 'react-bootstrap/Toast';
import styled from 'styled-components';

interface IToastConfig {
  title?: string;
  message?: string;
  showToast: boolean;
  setShowToast: React.Dispatch<React.SetStateAction<boolean>>;
}

const BottomLeftToast = styled(Toast)`
  position: 'absolute';
  top: 0;
  right: 0;
  margin: auto;
  text-align: center;
`;

export function CopyToast(props: IToastConfig) {
  const { title, message, showToast, setShowToast } = props;
  if (!showToast) {
    return null;
  }
  return (
    <>
      <BottomLeftToast
        show={showToast}
        onClose={() => setShowToast(false)}
        delay={3000}
        autohide
      >
        <Toast.Header>
          <strong className="mr-auto">{title || 'Success!'}</strong>
        </Toast.Header>
        <Toast.Body>{message || 'Shortlink copied to clipboard!'}</Toast.Body>
      </BottomLeftToast>
    </>
  );
}
