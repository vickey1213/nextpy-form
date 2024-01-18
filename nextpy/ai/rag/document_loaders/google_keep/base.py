# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""(Unofficial) Google Keep reader using gkeepapi."""

import json
import os
from typing import Any, List

from nextpy.ai.rag.document_loaders.basereader import BaseReader
from nextpy.ai.schema import DocumentNode


class GoogleKeepReader(BaseReader):
    """Google Keep reader.

    Reads notes from Google Keep

    """

    def load_data(self, document_ids: List[str]) -> List[DocumentNode]:
        """Load data from the document_ids.

        Args:
            document_ids (List[str]): a list of note ids.
        """
        keep = self._get_keep()

        if document_ids is None:
            raise ValueError('Must specify a "document_ids" in `load_kwargs`.')

        results = []
        for note_id in document_ids:
            note = keep.get(note_id)
            if note is None:
                raise ValueError(f"Note with id {note_id} not found.")
            text = f"Title: {note.title}\nContent: {note.text}"
            results.append(DocumentNode(text=text, extra_info={"note_id": note_id}))
        return results

    def load_all_notes(self) -> List[DocumentNode]:
        """Load all notes from Google Keep."""
        keep = self._get_keep()

        notes = keep.all()
        results = []
        for note in notes:
            text = f"Title: {note.title}\nContent: {note.text}"
            results.append(DocumentNode(text=text, extra_info={"note_id": note.id}))
        return results

    def _get_keep(self) -> Any:
        import gkeepapi

        """Get a Google Keep object with login."""
        # Read username and password from keep_credentials.json
        if os.path.exists("keep_credentials.json"):
            with open("keep_credentials.json", "r") as f:
                credentials = json.load(f)
        else:
            raise RuntimeError("Failed to load keep_credentials.json.")

        keep = gkeepapi.Keep()

        success = keep.login(credentials["username"], credentials["password"])
        if not success:
            raise RuntimeError("Failed to login to Google Keep.")

        return keep


if __name__ == "__main__":
    reader = GoogleKeepReader()
    print(
        reader.load_data(
            document_ids=[
                "1eKU7kGn8eJCErZ52OC7vCzHDSQaspFYGHHCiTX_IvhFOc7ZQZVJhTIDFMdTJOPiejOk"
            ]
        )
    )
