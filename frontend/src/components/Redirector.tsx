import { useEffect } from 'react';
import { BACKEND_URL } from '../config/settings';
import { useParams } from 'react-router-dom';

interface IKeyStr {
  key_str: string;
}

export function Redirector() {
  const { key_str } = useParams<IKeyStr>();
  useEffect(() => {
    const endpoint = `${BACKEND_URL}/shortlink/redirect/${key_str}`;
    window.location.href = endpoint;
  }, []);

  return null;
}
