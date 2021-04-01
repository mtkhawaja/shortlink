import React, { useState } from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';

interface IURLStr {
  shortlinkURL: string;
  originalURL?: string;
  setShowToast: React.Dispatch<React.SetStateAction<boolean>>;
}

export function ShortlinkModal(props: IURLStr) {
  const { shortlinkURL, originalURL, setShowToast } = props;
  if (!shortlinkURL) {
    return null;
  }
  const copyToClipboard = async (
    e: React.MouseEvent<HTMLElement, MouseEvent>
  ) => {
    await navigator.clipboard.writeText(shortlinkURL);
    setShowToast(true);
  };
  return (
    <>
      <Modal.Dialog className="text-center">
        <Modal.Body>
          <h5 className="text-truncate">
            Shortlink for{' '}
            <a
              href={originalURL}
              target="_blank"
              rel="noreferrer"
              aria-label={`Originally provided URL.`}
            >
              {originalURL}
            </a>
          </h5>
          <hr />
          <a
            href={shortlinkURL}
            target="_blank"
            rel="noreferrer"
            aria-label={`Shortlink for ${originalURL}`}
          >
            {shortlinkURL}
          </a>
        </Modal.Body>
        <Modal.Footer className="mx-auto">
          <Button onClick={copyToClipboard} variant="dark">
            Copy
          </Button>
        </Modal.Footer>
      </Modal.Dialog>
    </>
  );
}
