from db import DepOrm, new_session
from schemas import SDepAdd
from calc import ret_dep


class DepRepository:
    @classmethod
    async def add_dep(cls, dep: SDepAdd) -> dict:
        async with new_session() as session:
            data = dep.model_dump()
            new_dep = DepOrm(**data)
            session.add(new_dep)
            await session.flush()
            await session.commit()
            return ret_dep(dep)
