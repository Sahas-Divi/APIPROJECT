from fastapi import FastAPI, Response,status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oath2
from sqlalchemy.orm import Session


router = APIRouter(prefix = "/vote",tags = ["vote"])

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote : schemas.Vote, db : Session = Depends(database.get_db), current_user  = Depends(oath2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if post_query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "that post does not even exist")
    vote_query = db.query(models.Vote).filter(models.Vote.posts_id==vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
            detail = "user {} has already voted on post with id {}".format(current_user.id,vote.post_id))
        new_vote =  models.Vote(posts_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"sucessfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"successfully deleted vote"}